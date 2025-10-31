# daily_config.py

# --- I. DAMAGE PARAMETERS ---
# Updated DAILY based on OSINT reports on strike activity.
# This is the daily equivalent of the Week 43 intelligence.
AVG_STRIKES_PER_DAY = 3.5 / 7  # Converted from weekly
CRITICALITY_DIST = {
    'high': 0.70,
    'medium': 0.25,
    'low': 0.05
}
# DAMAGE_SCORES = {'high': 5, 'medium': 2, 'low': 1} # DEPRECATED
DAMAGE_DISTRIBUTIONS = {
    'high':   {'log_mean': 1.5, 'log_std': 0.5}, # Log-normal params for high impact
    'medium': {'log_mean': 0.6, 'log_std': 0.4},
    'low':    {'log_mean': 0.0, 'log_std': 0.3}
}

# --- II. REPAIR CAPACITY PARAMETERS ---
# Updated daily/weekly based on analysis of Russia's response capabilities.

# Baseline daily repair capacity
BASELINE_REPAIR_CAPACITY_PER_DAY = 10.7 / 7 # Abstract points per day.

# Modifiers from Week 43 Intelligence
SCENARIO_MODIFIER = 1.0 # Point Failure
TECH_DEPENDENCY_MODIFIER = 0.25 # High Dependency
POLITICAL_WILL_MODIFIER = 2.0 # High (direct Kremlin intervention)
HUMAN_CAPITAL_MODIFIER = 0.25 # High Impact

# --- III. SYSTEM HEALTH PARAMETERS ---
INITIAL_GRID_HEALTH = 100.0
COLLAPSE_THRESHOLD = 40.0 # Health % below which systemic consequence is triggered.

# --- IV. SIMULATION PARAMETERS ---
NUM_SIMULATIONS = 10000
TIME_HORIZON_DAYS = 24 * 7 # Forecast horizon (e.g., 6 months)
