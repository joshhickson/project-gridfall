# daily_simulator.py
import numpy as np
import daily_config as config  # Import the daily configuration file
from scipy.stats import lognorm

def run_daily_grid_simulation(days):
    """
    Runs a single simulation of grid health over a given number of days.
    Returns the day of collapse (1-indexed) or -1 if the grid survives.
    """
    grid_health = config.INITIAL_GRID_HEALTH

    for day in range(days):
        # 1. Calculate Damage for the Day using a probabilistic model
        num_strikes = np.random.poisson(config.AVG_STRIKES_PER_DAY)
        total_damage = 0
        for _ in range(num_strikes):
            target_type = np.random.choice(
                list(config.CRITICALITY_DIST.keys()),
                p=list(config.CRITICALITY_DIST.values())
            )
            # Draw from a log-normal distribution for more realistic damage impact
            params = config.DAMAGE_DISTRIBUTIONS[target_type]
            damage = lognorm.rvs(s=params['log_std'], scale=np.exp(params['log_mean']))
            total_damage += damage

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

    # --- Full Statistical Analysis ---
    if collapse_days:
        mean_collapse_day = np.mean(collapse_days)
        std_dev_collapse_day = np.std(collapse_days)
        percentile_25 = np.percentile(collapse_days, 25)
        median_collapse_day = np.median(collapse_days)
        percentile_75 = np.percentile(collapse_days, 75)
        percentile_95_tail_risk = np.percentile(collapse_days, 5) # 5th percentile for earliest collapse
    else:
        mean_collapse_day = -1
        std_dev_collapse_day = -1
        percentile_25 = -1
        median_collapse_day = -1
        percentile_75 = -1
        percentile_95_tail_risk = -1

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
    print(f"\n--- DAILY TIMELINE ANALYSIS (STATISTICAL SUMMARY) ---")
    if probability_of_collapse > 0:
        print(f"  - Mean Collapse Point:    Day {mean_collapse_day:.1f} (Std Dev: {std_dev_collapse_day:.1f})")
        print(f"  - Interquartile Range:    Day {percentile_25:.1f} to {percentile_75:.1f}")
        print(f"  - Median Collapse Point:  Day {median_collapse_day:.1f}")
        print(f"  - 5% Tail Risk Point:     Collapse by Day {percentile_95_tail_risk:.1f}")
    else:
        print("  - No systemic collapse predicted within the time horizon.")
    print("="*52)
    print(f"\nESTIMATED PROBABILITY OF SYSTEMIC CONSEQUENCE: {probability_of_collapse:.2f}%\n")

if __name__ == "__main__":
    main()
