### **Project Brief & Implementation Guide for AI Developer**

**Project Title:** Predictive Simulator for Russian Energy Grid Stability (Project "Fertilizer-Proxy")

**To:** Google Jules (AI Developer)

**From:** Project Lead

**Date:** October 30, 2025

**Objective:** Your primary task is to develop a Python-based Monte Carlo simulator based on the analytical work contained within this GitHub repository. The entire conversation history and all attached reports serve as your knowledge base.

The simulator's core function is to forecast the probability of a systemic collapse of Russia's energy grid over a defined time horizon. This model will serve as a strategic proxy for predicting the operational stability and production rate of Russia's energy-intensive fertilizer industry.

**Core Logic & Architecture:** The simulator will model the attritional conflict between Ukrainian strikes on Russian energy infrastructure (damage) and Russia's ability to recover from that damage (repair). The final output will be a probability percentage derived from running thousands of simulations.

**Step-by-Step Implementation Instructions:**

**Step 1: Project Setup & Version Control**

1.  Initialize a new Git repository for this project.

2.  Create the following file structure:

    *   `simulator.py` (The main simulation engine)

    *   `config.py` (User-configurable parameters)

    *   `changelog.md` (A log of all development work)

    *   `README.md` (This document)


**Step 2: Version Control & Commit Logging Protocol**

This is a strict requirement. Before every `git commit`, you must log a description of the work you are about to commit in the `changelog.md` file.

1.  Open `changelog.md`.

2.  Append a new entry using the following markdown format:

    YYYY-MM-DD HH:MM:SS
    -------------------

    *   \[Add more bullet points if necessary for complex commits.\]


    * * *

3.  Save the `changelog.md` file.

4.  Stage all your changed files (`git add.`).

5.  Commit your changes with a descriptive message (e.g., `git commit -m "feat: Implement multi-factor repair capacity logic"`).


**Step 3: Create the Configuration File (`config.py`)**

This file will hold all variables the user will update weekly. This separation is critical for ease of use. Populate `config.py` with the following structure and default values:

Python

```
# config.py

# --- I. DAMAGE PARAMETERS ---
# Updated weekly based on OSINT reports on strike activity.
AVG_STRIKES_PER_WEEK = 5.5
CRITICALITY_DIST = {
    'high': 0.30,   # e.g., 750kV/500kV substation, major power plant
    'medium': 0.50, # e.g., refinery, smaller substation, rail power
    'low': 0.20     # e.g., transmission lines, minor depot
}
DAMAGE_SCORES = {'high': 5, 'medium': 2, 'low': 1}

# --- II. REPAIR CAPACITY PARAMETERS ---
# Updated weekly/monthly based on analysis of Russia's response capabilities.

# Baseline derived from the Sayano-Shushenskaya HPP reconstruction (107 MW/month).
# Represents a "normal" major project footing.
BASELINE_REPAIR_CAPACITY = 10.7 # Abstract points per week.

# 1. SCENARIO MODIFIER: Reflects the nature of the damage.
#    0.5 = Dispersed Damage (strains logistics)
#    1.0 = Point Failure (focused effort, baseline)
#    1.5 = Strategic Priority (accelerated effort)
SCENARIO_MODIFIER = 1.0

# 2. TECHNOLOGY DEPENDENCY MODIFIER: Reflects sanctions impact.
#    0.25 = High Dependency (e.g., advanced gas turbines, SCADA systems hit)
#    1.0 = High Sovereignty (e.g., hydropower, standard transmission hit)
TECH_DEPENDENCY_MODIFIER = 1.0

# 3. POLITICAL WILL MODIFIER: Acts as an accelerator.
#    1.0 = Medium (standard response)
#    2.0 = High (direct Kremlin intervention)
POLITICAL_WILL_MODIFIER = 1.0

# 4. HUMAN CAPITAL MODIFIER: Long-term degradation from brain drain.
#    Starts at 1.0 and can be slowly decayed over time.
HUMAN_CAPITAL_MODIFIER = 1.0

# --- III. SYSTEM HEALTH PARAMETERS ---
INITIAL_GRID_HEALTH = 100.0
COLLAPSE_THRESHOLD = 40.0 # Health % below which systemic consequence is triggered.

# --- IV. SIMULATION PARAMETERS ---
NUM_SIMULATIONS = 10000
TIME_HORIZON_WEEKS = 24 # Forecast horizon (e.g., 6 months)
```

**Step 4: Create the Simulator Engine (`simulator.py`)**

Write the main Python script. It must import the configuration, run the simulation, and print a clear, readable output.

Python

```
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
```

**Step 5: Final Instructions**

Your final task is to create the `README.md` file containing these instructions. This ensures that the purpose, architecture, and workflow of the project are clearly documented for the user.

This concludes the setup. You are now authorized to begin development.