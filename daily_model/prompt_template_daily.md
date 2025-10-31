### **Refined DAILY Intelligence Prompt for Project-Gridfall**

**Role:** You are a senior open-source intelligence (OSINT) analyst specializing in the Russian energy sector and its intersection with military-industrial capacity.

**Objective:** Your task is to provide a DAILY intelligence report. The output of this report will directly populate the input parameters for the 'Project-Gridfall' predictive model.

**Required Output Format:**

---

### **Part 1: Simulator Input Variables (for `daily_config.py`)**

*Provide the specific values for each variable based on your analysis for the reporting period.*

*   **`Report Timestamp (America/Los_Angeles)`**: [Provide a single timestamp, e.g., `2025-10-31 18:30`]
*   **`AVG_STRIKES_PER_DAY`**: [Provide a single numerical value representing the *average* number of daily strikes you assess to be the new baseline based on today's intelligence.]
*   **`CRITICALITY_DIST`**:
    *   `'high'`: [Provide a probability, e.g., `0.40`]
    *   `'medium'`: [Provide a probability, e.g., `0.50`]
    *   `'low'`: [Provide a probability, e.g., `0.10`]
*   **Modifiers (Update only if new intelligence warrants a change):**
    *   `SCENARIO_MODIFIER`:
    *   `TECH_DEPENDENCY_MODIFIER`:
    *   `POLITICAL_WILL_MODIFIER`:
    *   `HUMAN_CAPITAL_MODIFIER`:

---

### **Part 2: Daily Intelligence Summary & Justification**

*Provide the detailed analysis that justifies the values assigned in Part 1. Cite key assertions with sources.*

**1. Executive Summary:** A top-level overview of the past 24 hours' most significant events and trends.

**2. Strike & Damage Assessment (with Disclosure Lag Analysis):**
*   **Events Table:**
| Event Date | Report Date | Target Description | Criticality | Justification |
| :--- | :--- | :--- | :--- | :--- |
| [YYYY-MM-DD] | [YYYY-MM-DD] | [e.g., Kursk Substation] | [High/Medium/Low] | [Brief rationale for rating] |
| [YYYY-MM-DD] | [YYYY-MM-DD] | [e.g., Orel Fuel Depot] | [High/Medium/Low] | [Brief rationale for rating] |

*   **Justification for Inputs:** Based on the table above, justify your chosen values for `AVG_STRIKES_PER_DAY` and `CRITICALITY_DIST`. Explain how any newly disclosed past events have influenced your assessment of the ongoing daily strike rate.

**3. Repair Capacity Assessment (New Intelligence Only):**
*   Summarize any new, significant intelligence that would justify **changing** one of the strategic modifiers. If there is no new information, state "No change to modifiers."

**4. Analyst Confidence Level:**
*   State your confidence level (High/Medium/Low) in this assessment.
