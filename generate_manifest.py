# generate_manifest.py
import csv
from datetime import datetime, timedelta

def get_mondays_in_range(start_date, end_date):
    """Yields the Monday of each week within a given date range."""
    current_date = start_date
    while current_date <= end_date:
        if current_date.weekday() == 0: # 0 is Monday
            yield current_date
        current_date += timedelta(days=1)

def generate_manifest(filename, phases):
    """
    Generates a CSV manifest file with date ranges for historical data collection.
    """
    header = ['start_date_utc', 'end_date_utc', 'report_filename', 'status']

    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)

        for phase_name, (start_str, end_str) in phases.items():
            start_date = datetime.strptime(start_str, '%Y-%m-%d')
            end_date = datetime.strptime(end_str, '%Y-%m-%d')

            # Write a header row for the phase
            writer.writerow([f"--- PHASE: {phase_name} ---", "", "", ""])

            for monday in get_mondays_in_range(start_date, end_date):
                sunday = monday + timedelta(days=6)

                # Ensure we don't go past the phase's end date
                if sunday > end_date:
                    continue

                start_fmt = monday.strftime('%Y-%m-%d')
                end_fmt = sunday.strftime('%Y-%m-%d')
                filename_fmt = f"{start_fmt}_report.md"

                writer.writerow([start_fmt, end_fmt, filename_fmt, 'Pending'])

    print(f"Successfully generated data collection manifest: {filename}")

if __name__ == '__main__':
    # Define the two phases of data collection as requested by the user.
    # Phase 1: Recent data (July 22, 2025 to nearest present-day week)
    # Phase 2: Deeper history (October 21, 2024 to July 21, 2025)

    # We'll set the "present day" to the end of the last full week.
    # Today is Nov 1, 2025. The last full week ended on Oct 26, 2025.

    collection_phases = {
        "Phase 1 (Recent History)": ('2025-07-22', '2025-10-26'),
        "Phase 2 (Deep History)": ('2024-10-21', '2025-07-21')
    }

    output_file = 'historical_data_manifest.csv'

    generate_manifest(output_file, collection_phases)
