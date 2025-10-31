# backtester.py
import json
import simulator
import config as main_config
import numpy as np

def run_backtest(history_file):
    """
    Loads historical data, runs the simulator for each period, and prints the forecast.
    """
    try:
        with open(history_file, 'r') as f:
            historical_data = json.load(f)
    except FileNotFoundError:
        print(f"Error: History file not found at {history_file}")
        return

    print("--- STARTING HISTORICAL BACKTEST ---")

    for period in historical_data:
        print("\n" + "="*50)
        print(f"  RUNNING SIMULATION FOR PERIOD: {period['period_id']} ({period['start_date']} to {period['end_date']})")
        print("="*50)
        print(f"Notes: {period['notes']}")

        # --- Dynamic Re-configuration ---
        # Override the default config values with the historical data for this period
        for key, value in period['input_variables'].items():
            setattr(main_config, key, value)

        # Run the main simulation function from the simulator module
        # Note: We are calling the main() function which contains the full simulation and print logic.
        # A more advanced version might refactor simulator.py to separate the core simulation
        # logic from the printing, but this is a robust starting point.
        simulator.main()

    print("\n--- HISTORICAL BACKTEST COMPLETE ---")

if __name__ == '__main__':
    # We will use the sample file for this framework test.
    # In the future, this could take a command-line argument for the file path.
    run_backtest('historical_data/sample_weekly_history.json')
