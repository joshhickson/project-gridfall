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
