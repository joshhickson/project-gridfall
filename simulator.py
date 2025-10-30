# simulator.py
import numpy as np
import config  # Import the configuration file

def run_grid_simulation(weeks):
    """Runs a single simulation of grid health over a given number of weeks."""
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
            return True  # Systemic consequence occurred

    return False  # Survived the time horizon

def main():
    """Main function to run the Monte Carlo simulation and print results."""
    collapse_count = 0
    for _ in range(config.NUM_SIMULATIONS):
        if run_grid_simulation(config.TIME_HORIZON_WEEKS):
            collapse_count += 1

    probability_of_collapse = (collapse_count / config.NUM_SIMULATIONS) * 100

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
    print(f"\nESTIMATED PROBABILITY OF SYSTEMIC CONSEQUENCE: {probability_of_collapse:.2f}%\n")

if __name__ == "__main__":
    main()
