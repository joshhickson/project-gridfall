# simulator.py
import numpy as np
import config  # Import the configuration file

def run_grid_simulation(weeks):
    """
    Runs a single simulation of grid health over a given number of weeks.
    Returns the week of collapse (1-indexed) or -1 if the grid survives.
    """
    grid_health = config.INITIAL_GRID_HEALTH

    for week in range(weeks):
        # 1. Calculate Damage for the Week
        num_strikes = np.random.poisson(config.AVG_STRIKES_PER_WEEK)
        total_damage = 0
        for _ in range(num_strikes):
            target_type = np.random.choice(
                list(config.CRITICALITY_DIST.keys()),
                p=list(config.CRITICALITY_DIST.values())
            )
            total_damage += config.DAMAGE_SCORES[target_type]

        # 2. Calculate MODIFIED Repair Capacity for the Week
        actual_repair_this_week = (config.BASELINE_REPAIR_CAPACITY *
                                   config.SCENARIO_MODIFIER *
                                   config.TECH_DEPENDENCY_MODIFIER *
                                   config.POLITICAL_WILL_MODIFIER *
                                   config.HUMAN_CAPITAL_MODIFIER)

        # 3. Apply Damage and Repair
        grid_health -= total_damage
        grid_health += actual_repair_this_week
        grid_health = min(grid_health, 100.0) # Health cannot exceed 100%

        # 4. Check for Collapse
        if grid_health <= config.COLLAPSE_THRESHOLD:
            return week + 1  # Systemic consequence occurred, return week number (1-indexed)

    return -1  # Survived the time horizon

def main():
    """Main function to run the Monte Carlo simulation and print results."""
    collapse_weeks = []
    for _ in range(config.NUM_SIMULATIONS):
        collapse_week = run_grid_simulation(config.TIME_HORIZON_WEEKS)
        if collapse_week != -1:
            collapse_weeks.append(collapse_week)

    probability_of_collapse = (len(collapse_weeks) / config.NUM_SIMULATIONS) * 100

    # --- New statistical analysis ---
    if collapse_weeks:
        median_collapse_week = np.median(collapse_weeks)
        # Using a simple method for mode; for more complex distributions, scipy.stats.mode might be better
        week_counts = np.bincount(collapse_weeks)
        mode_collapse_week = np.argmax(week_counts)
    else:
        median_collapse_week = -1
        mode_collapse_week = -1

    # Calculate the final repair capacity used in the simulation
    final_repair_capacity = (config.BASELINE_REPAIR_CAPACITY *
                             config.SCENARIO_MODIFIER *
                             config.TECH_DEPENDENCY_MODIFIER *
                             config.POLITICAL_WILL_MODIFIER *
                             config.HUMAN_CAPITAL_MODIFIER)

    # Print a clear, formatted output
    print("--- RUSSIAN ENERGY GRID STABILITY FORECAST ---")
    print("="*44)
    print(f"SIMULATION PARAMETERS:")
    print(f"  - Time Horizon:         {config.TIME_HORIZON_WEEKS} weeks")
    print(f"  - Number of Simulations:  {config.NUM_SIMULATIONS:,}")
    print(f"  - Collapse Threshold:     {config.COLLAPSE_THRESHOLD}% Grid Health")
    print("\nINPUT VARIABLES (from config.py):")
    print(f"  - Avg Weekly Strikes:     {config.AVG_STRIKES_PER_WEEK}")
    print(f"  - Scenario Modifier:      {config.SCENARIO_MODIFIER}")
    print(f"  - Tech Dependency Mod:    {config.TECH_DEPENDENCY_MODIFIER}")
    print(f"  - Political Will Mod:     {config.POLITICAL_WILL_MODIFIER}")
    print(f"  - Human Capital Mod:      {config.HUMAN_CAPITAL_MODIFIER}")
    print(f"  - Resulting Repair Rate:  {final_repair_capacity:.2f} points/week")
    print("="*44)
    print(f"\n--- TIMELINE ANALYSIS ---")
    if probability_of_collapse > 0:
        print(f"  - Median Collapse Point:  Week {median_collapse_week:.0f}")
        print(f"  - Most Likely Collapse:   Week {mode_collapse_week}")
    else:
        print("  - No systemic collapse predicted within the time horizon.")
    print("="*44)
    print(f"\nESTIMATED PROBABILITY OF SYSTEMIC CONSEQUENCE: {probability_of_collapse:.2f}%\n")


if __name__ == "__main__":
    main()
