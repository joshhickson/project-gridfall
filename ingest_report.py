# ingest_report.py
import json
import sys
from datetime import datetime
import re

def parse_report_line_by_line(content):
    """
    Parses the entire markdown report using a more robust line-by-line, non-regex approach.
    """
    data = {}
    lines = content.split('\n')

    # A more precise regex to find the value inside '[`...`]'
    value_regex = re.compile(r'\[`?([^`\]]+)`?\]')

    in_vars_section = False
    for i, line in enumerate(lines):
        line = line.strip()

        if "Part 1: Simulator Input Variables" in line:
            in_vars_section = True
        if "Part 2:" in line and in_vars_section:
            in_vars_section = False

        if not line.startswith('*'):
            continue

        # --- Parse Metadata ---
        if '`period_id`' in line:
            match = value_regex.search(line)
            if match:
                data['period_id'] = match.group(1).strip()

        # --- Parse Input Variables ---
        if in_vars_section:
            if '`AVG_STRIKES_PER_WEEK`' in line:
                match = value_regex.search(line)
                if match:
                    data['AVG_STRIKES_PER_WEEK'] = float(match.group(1).strip())

            elif '`POLITICAL_WILL_MODIFIER`' in line:
                match = value_regex.search(line)
                if match:
                    data['POLITICAL_WILL_MODIFIER'] = float(match.group(1).strip())

            elif "`CRITICALITY_DIST`" in line:
                dist = {}
                try:
                    # Look ahead for the distribution lines, which are not guaranteed to be right after
                    for j in range(i + 1, len(lines)):
                        sub_line = lines[j].strip()
                        if not sub_line.startswith('*'): continue
                        if "'high'" in sub_line:
                            match = value_regex.search(sub_line)
                            if match: dist['high'] = float(match.group(1).strip())
                        elif "'medium'" in sub_line:
                            match = value_regex.search(sub_line)
                            if match: dist['medium'] = float(match.group(1).strip())
                        elif "'low'" in sub_line:
                            match = value_regex.search(sub_line)
                            if match: dist['low'] = float(match.group(1).strip())

                        if len(dist) == 3:
                            break # Found all three
                    data['CRITICALITY_DIST'] = dist
                except (IndexError, ValueError):
                     data['CRITICALITY_DIST'] = None # Failed to parse

    return data


def ingest_report(report_file, master_history_file):
    """Parses a markdown report and appends its data to the master JSON history."""
    print(f"--- Starting ingestion for {report_file} ---")
    try:
        with open(report_file, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: Report file not found at {report_file}")
        return

    # --- Data Extraction ---
    parsed_data = parse_report_line_by_line(content)

    if 'period_id' not in parsed_data or not parsed_data['period_id']:
        print("Error: Could not parse period_id from report.")
        return

    # --- Construct the JSON Object ---
    new_entry = {
        "period_id": parsed_data.get('period_id'),
        "ingestion_date": datetime.utcnow().isoformat(),
        "source_file": report_file,
        "notes": "Ingested via ingest_report.py",
        "input_variables": {
            "AVG_STRIKES_PER_WEEK": parsed_data.get('AVG_STRIKES_PER_WEEK'),
            "CRITICALITY_DIST": parsed_data.get('CRITICALITY_DIST'),
            "SCENARIO_MODIFIER": 1.0, # Placeholder
            "TECH_DEPENDENCY_MODIFIER": 1.0, # Placeholder
            "POLITICAL_WILL_MODIFIER": parsed_data.get('POLITICAL_WILL_MODIFIER'),
            "HUMAN_CAPITAL_MODIFIER": 1.0 # Placeholder
        }
    }

    # --- Append to Master History File ---
    try:
        with open(master_history_file, 'r', encoding='utf-8') as f:
            history = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        history = []

    # Prevent duplicate entries by updating existing ones if found
    entry_found = False
    for i, entry in enumerate(history):
        if entry.get('period_id') == new_entry['period_id']:
            print(f"Updating existing entry for period '{new_entry['period_id']}'.")
            history[i] = new_entry
            entry_found = True
            break

    if not entry_found:
        print(f"Adding new entry for period '{new_entry['period_id']}'.")
        history.append(new_entry)

    with open(master_history_file, 'w', encoding='utf-8') as f:
        json.dump(history, f, indent=4)

    print(f"Successfully ingested/updated report in {master_history_file}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 ingest_report.py <path_to_markdown_report>")
        sys.exit(1)

    report_path = sys.argv[1]
    master_file = 'historical_data/master_weekly_history.json'
    ingest_report(report_path, master_file)
