# daily_simulator.py
import numpy as np
import daily_config as config  # Import the daily configuration file
import json
from datetime import datetime

def run_daily_grid_simulation(days):
    """
    Runs a single simulation of grid health over a given number of days.
    Returns the day of collapse (1-indexed) or -1 if the grid survives.
    """
    grid_health = config.INITIAL_GRID_HEALTH

    for day in range(days):
        # 1. Calculate Damage for the Day
        num_strikes = np.random.poisson(config.AVG_STRIKES_PER_DAY)
        total_damage = 0
        for _ in range(num_strikes):
            target_type = np.random.choice(
                list(config.CRITICALITY_DIST.keys()),
                p=list(config.CRITICALITY_DIST.values())
            )
            total_damage += config.DAMAGE_SCORES[target_type]

        # 2. Calculate MODIFIED Repair Capacity for the Day
        actual_repair_this_day = (config.BASELINE_REPAIR_CAPACITY_PER_DAY *
                                   config.SCENARIO_MODIFIER *
                                   config.TECH_DEPENDENCY_MODIFIER *
                                   config.POLITICAL_WILL_MODIFIER *
                                   config.HUMAN_CAPITAL_MODIFIER)

        # 3. Apply Damage and Repair
        grid_health -= total_damage
        grid_health += actual_repair_this_day
        grid_health = min(grid_health, 100.0) # Health cannot exceed 100%

        # 4. Check for Collapse
        if grid_health <= config.COLLAPSE_THRESHOLD:
            return day + 1  # Systemic consequence occurred, return day number (1-indexed)

    return -1  # Survived the time horizon

def main():
    """Main function to run the Monte Carlo simulation and print results."""
    collapse_days = []
    for _ in range(config.NUM_SIMULATIONS):
        collapse_day = run_daily_grid_simulation(config.TIME_HORIZON_DAYS)
        if collapse_day != -1:
            collapse_days.append(collapse_day)

    probability_of_collapse = (len(collapse_days) / config.NUM_SIMULATIONS) * 100

    # --- New statistical analysis ---
    if collapse_days:
        median_collapse_day = np.median(collapse_days)
        day_counts = np.bincount(collapse_days)
        mode_collapse_day = np.argmax(day_counts)
    else:
        median_collapse_day = -1
        mode_collapse_day = -1

    # Calculate the final repair capacity used in the simulation
    final_repair_capacity = (config.BASELINE_REPAIR_CAPACITY_PER_DAY *
                             config.SCENARIO_MODIFIER *
                             config.TECH_DEPENDENCY_MODIFIER *
                             config.POLITICAL_WILL_MODIFIER *
                             config.HUMAN_CAPITAL_MODIFIER)

    # Print a clear, formatted output
    print("--- DAILY: RUSSIAN ENERGY GRID STABILITY FORECAST ---")
    print("="*52)
    print(f"SIMULATION PARAMETERS:")
    print(f"  - Time Horizon:         {config.TIME_HORIZON_DAYS} days")
    print(f"  - Number of Simulations:  {config.NUM_SIMULATIONS:,}")
    print(f"  - Collapse Threshold:     {config.COLLAPSE_THRESHOLD}% Grid Health")
    print("\nINPUT VARIABLES (from daily_config.py):")
    print(f"  - Avg Daily Strikes:      {config.AVG_STRIKES_PER_DAY:.2f}")
    print(f"  - Scenario Modifier:      {config.SCENARIO_MODIFIER}")
    print(f"  - Tech Dependency Mod:    {config.TECH_DEPENDENCY_MODIFIER}")
    print(f"  - Political Will Mod:     {config.POLITICAL_WILL_MODIFIER}")
    print(f"  - Human Capital Mod:      {config.HUMAN_CAPITAL_MODIFIER}")
    print(f"  - Resulting Repair Rate:  {final_repair_capacity:.2f} points/day")
    print("="*52)
    print(f"\n--- DAILY TIMELINE ANALYSIS ---")
    if probability_of_collapse > 0:
        print(f"  - Median Collapse Point:  Day {median_collapse_day:.0f}")
        print(f"  - Most Likely Collapse:   Day {mode_collapse_day}")
    else:
        print("  - No systemic collapse predicted within the time horizon.")
    print("="*52)
    print(f"\nESTIMATED PROBABILITY OF SYSTEMIC CONSEQUENCE: {probability_of_collapse:.2f}%\n")

    # --- Save results to a separate daily history file ---
    history_file = 'daily_model/simulation_history_daily.json'

    output_data = {
        'timestamp': datetime.utcnow().isoformat(),
        'model_type': 'daily',
        'simulation_parameters': {
            'time_horizon_days': config.TIME_HORIZON_DAYS,
            'num_simulations': config.NUM_SIMULATIONS,
            'collapse_threshold': config.COLLAPSE_THRESHOLD
        },
        'input_variables': {
            'avg_strikes_per_day': config.AVG_STRIKES_PER_DAY,
            'criticality_dist': config.CRITICALITY_DIST,
            'scenario_modifier': config.SCENARIO_MODIFIER,
            'tech_dependency_modifier': config.TECH_DEPENDENCY_MODIFIER,
            'political_will_modifier': config.POLITICAL_WILL_MODIFIER,
            'human_capital_modifier': config.HUMAN_CAPITAL_MODIFIER
        },
        'forecast': {
            'probability_of_collapse': probability_of_collapse,
            'median_collapse_day': int(median_collapse_day) if median_collapse_day != -1 else None,
            'mode_collapse_day': int(mode_collapse_day) if mode_collapse_day != -1 else None
        }
    }

    try:
        with open(history_file, 'r') as f:
            history = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        history = []

    history.append(output_data)

    with open(history_file, 'w') as f:
        json.dump(history, f, indent=4)

    print(f"Results saved to {history_file}")


if __name__ == "__main__":
    main()
