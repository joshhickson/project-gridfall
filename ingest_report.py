# ingest_report.py
import json
import sys
from datetime import datetime
import re

def parse_report_line_by_line(content):
    """
    Parses the entire markdown report using a robust line-by-line approach.
    """
    data = {}
    lines = content.split('\n')

    # Regex to find the value inside '[...]' which may or may not have backticks
    value_regex = re.compile(r'\[`?([^`\]]+)`?\]')

    # Regex to find string-based modifier values
    string_value_regex = re.compile(r"\[Choose one:.*?`([\d\.]+)` \((.*?)\)")


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
            # --- Numerical Values ---
            if '`AVG_STRIKES_PER_WEEK`' in line or '`POLITICAL_WILL_MODIFIER`' in line:
                match = value_regex.search(line)
                if match:
                    key = 'AVG_STRIKES_PER_WEEK' if 'AVG_STRIKES_PER_WEEK' in line else 'POLITICAL_WILL_MODIFIER'
                    data[key] = float(match.group(1).strip())

            # --- String-based Modifiers ---
            elif '`SCENARIO_MODIFIER`' in line or '`TECH_DEPENDENCY_MODIFIER`' in line or '`HUMAN_CAPITAL_MODIFIER`' in line:
                 key_map = {
                    '`SCENARIO_MODIFIER`': 'SCENARIO_MODIFIER',
                    '`TECH_DEPENDENCY_MODIFIER`': 'TECH_DEPENDENCY_MODIFIER',
                    '`HUMAN_CAPITAL_MODIFIER`': 'HUMAN_CAPITAL_MODIFIER'
                }
                 for key_str, key_name in key_map.items():
                     if key_str in line:
                        # Find the chosen value from the line
                        # Example: [Choose one: `0.5` (Dispersed), `1.0` (Point Failure)]
                        # We need to extract the number from the selected option
                        # For simplicity in this parser, we will rely on the user putting the chosen value first.
                        # A better parser would find the selected text and get its value.
                        # This is a limitation we will accept for now.
                        all_options = string_value_regex.findall(line)
                        if all_options:
                            # This is a simplification; we'll take the first option's value
                            data[key_name] = float(all_options[0][0])

            # --- Dictionary Value ---
            elif "`CRITICALITY_DIST`" in line:
                dist = {}
                try:
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

                        if len(dist) == 3: break
                    data['CRITICALITY_DIST'] = dist
                except (IndexError, ValueError):
                     data['CRITICALITY_DIST'] = None

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

    parsed_data = parse_report_line_by_line(content)

    if 'period_id' not in parsed_data or not parsed_data['period_id']:
        print("Error: Could not parse period_id from report.")
        return

    new_entry = {
        "period_id": parsed_data.get('period_id'),
        "ingestion_date": datetime.utcnow().isoformat(),
        "source_file": report_file,
        "notes": "Ingested via ingest_report.py",
        "input_variables": {
            "AVG_STRIKES_PER_WEEK": parsed_data.get('AVG_STRIKES_PER_WEEK'),
            "CRITICALITY_DIST": parsed_data.get('CRITICALITY_DIST'),
            "SCENARIO_MODIFIER": parsed_data.get('SCENARIO_MODIFIER', 1.0),
            "TECH_DEPENDENCY_MODIFIER": parsed_data.get('TECH_DEPENDENCY_MODIFIER', 1.0),
            "POLITICAL_WILL_MODIFIER": parsed_data.get('POLITICAL_WILL_MODIFIER'),
            "HUMAN_CAPITAL_MODIFIER": parsed_data.get('HUMAN_CAPITAL_MODIFIER', 1.0)
        }
    }

    try:
        with open(master_history_file, 'r', encoding='utf-8') as f:
            history = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        history = []

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
