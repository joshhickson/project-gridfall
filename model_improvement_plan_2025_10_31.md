# Project-Gridfall: Model Improvement & Validation Plan
**Document Date:** 2025-10-31 00:23 UTC
**Author:** Jules, AI Developer & Analyst

---

### **Preamble: From Alpha to Actuarial**

The following is a detailed, multi-phase gameplan to mature Project-Gridfall from its current state as a promising **Alpha Model** into a robust, validated, and **Actuarially Sound** predictive instrument. The objective is to systematically address the current weaknesses in the model to increase its accuracy, reliability, and the confidence with which its outputs can be used for strategic decision-making.

---

### **Phase 1: Foundational Model Enhancements (Target: Q4 2025 - Q1 2026)**

*This phase addresses the most immediate and critical flaws in the model's core logic: the arbitrary damage scores and the incomplete statistical output.*

#### **1.1. Task: Implement Full Distribution Statistical Output**
*   **Problem:** The current model only outputs the median and mode of the collapse timeline. This gives a point estimate but fails to describe the full "shape of the risk."
*   **Action:**
    1.  Modify the `main` function in both `simulator.py` and `daily_model/daily_simulator.py`.
    2.  In addition to median and mode, the script will calculate and store the **mean**, **standard deviation**, and key **percentiles** (25th, 75th, and the critical 95th for "catastrophic tail risk").
    3.  The final printout will be enhanced to display this new, richer statistical summary.
*   **Justification:** This provides a far more complete picture of the forecast. Understanding the standard deviation tells us how much confidence we have in the mean, while the 95th percentile tells us the worst-case scenario we need to be prepared for. This is a standard requirement for any serious risk modeling.

#### **1.2. Task: Implement Probabilistic Damage Model**
*   **Problem:** The `DAMAGE_SCORES = {'high': 5, 'medium': 2, 'low': 1}` system is the single greatest weakness, being arbitrary and linear.
*   **Action:**
    1.  The `config.py` and `daily_config.py` files will be modified. The static `DAMAGE_SCORES` dictionary will be replaced with parameters for a statistical distribution. A **log-normal distribution** is recommended as a starting point, as it better models the low-probability, high-impact nature of strategic events.
    2.  The configuration would change to look like this: `DAMAGE_DISTRIBUTIONS = {'high': {'mean': 3.0, 'std_dev': 1.5}, 'medium': ...}`.
    3.  The core simulation logic will be updated. Instead of a simple lookup, it will call a function that draws a random value from the specified log-normal distribution for each strike. This will require adding the `scipy` library to our dependencies.
*   **Justification:** This addresses the "actuarially unsound" nature of the damage model. It replaces a guess with a statistically rigorous and defensible method that acknowledges the nonlinear, cascading impact of high-criticality events.

---

### **Phase 2: Historical Validation & Calibration (Target: Q1-Q2 2026)**

*This phase addresses the critical need to tether the model to reality by testing it against historical data.*

#### **2.1. Task: Develop Historical Data Ingestion Framework**
*   **Problem:** The model has not been validated against the past. We need a structured way to feed it historical data.
*   **Action:**
    1.  Define a clear, structured format (likely CSV or JSON) for historical intelligence reports. The format will mirror our daily/weekly prompt structure.
    2.  Create a new Python script, `backtester.py`, which is designed to read this historical data file, loop through it chronologically, and run the simulator for each time step.
*   **Justification:** This creates the necessary tooling for a repeatable, scientific back-testing process.

#### **2.2. Task: Execute Back-testing (Data Collection & Analysis)**
*   **Problem:** The model's assumptions have not been tested.
*   **Action:**
    1.  **(Human-Intensive Task)** An analyst must be tasked with collecting and structuring OSINT from the past 12-18 months into the format defined in Task 2.1.
    2.  Run the `backtester.py` script on the full historical dataset.
    3.  The script will output a timeline of the model's simulated "grid health" vs. the actual, qualitative assessments from the historical reports.
*   **Justification:** This is the most critical step for building confidence. If the model's simulated health drops during periods we know were difficult for the Russian grid, it validates our core logic. If not, it tells us our fundamental assumptions are wrong and need to be re-evaluated.

#### **2.3. Task: Model Calibration**
*   **Problem:** The model's parameters are currently expert estimates. They need to be data-driven.
*   **Action:**
    1.  Based on the results of the back-test, systematically tune the parameters in the `config.py` file (e.g., the means and standard deviations of the damage distributions, the baseline repair capacity).
    2.  The goal is to find the set of parameters that minimizes the difference between the model's output and historical reality.
*   **Justification:** This turns our expert-driven model into an empirically-grounded one, significantly increasing its credibility and predictive power.

---

### **Phase 3: Advanced Analysis (Target: Q2-Q3 2026)**

*With a validated and calibrated model, we can move to more advanced analytical techniques.*

#### **3.1. Task: Implement Sensitivity Analysis Module**
*   **Problem:** We don't have a quantified understanding of which variables drive the forecast.
*   **Action:**
    1.  Create a new function or script that systematically runs the simulation multiple times, varying a single input modifier (e.g., `TECH_DEPENDENCY_MODIFIER`) across its full range while holding all others constant.
    2.  The output will be a chart showing how the median collapse date changes as the input modifier changes.
*   **Justification:** This will provide a "Tornado Chart" of model sensitivities, telling us exactly which variables are the most powerful levers in the system. This is invaluable for focusing our limited intelligence-gathering resources on the factors that matter most.

#### **3.2. Task: Model Modifier Interdependencies**
*   **Problem:** The model incorrectly assumes all strategic modifiers are independent.
*   **Action:** This is a research task. Using the historical dataset from Phase 2, perform a statistical correlation analysis. For example, is there a statistically significant correlation between a change in the `POLITICAL_WILL_MODIFIER` and a subsequent change in the `HUMAN_CAPITAL_MODIFIER`?
*   **Justification:** The results of this research would form the basis for a future "Phase 4" model, which would replace the simple multipliers with a more sophisticated, interconnected system (e.g., a Bayesian network or a system dynamics model) that captures the true complexity of the operating environment.
