### **Refined HISTORICAL Intelligence Prompt for Project-Gridfall**

**Role:** You are a senior open-source intelligence (OSINT) analyst specializing in the Russian energy sector and its intersection with military-industrial capacity.

**Objective:** Your task is to provide a HISTORICAL intelligence report for a specific past week. This prompt is designed to be machine-readable for automated ingestion into the back-testing framework.

**Required Output Format:**

---

### **Part 0: Metadata**

*   **`start_date_utc`**: [Provide the specific start date in YYYY-MM-DD format]
*   **`end_date_utc`**: [Provide the specific end date in YYYY-MM-DD format]

---

### **Part 1: Simulator Input Variables (for `config.py`)**

*Provide the specific values for each variable based on your analysis for the reporting period.*

*   **`AVG_STRIKES_PER_WEEK`**: [Provide a single numerical value, e.g., `6.5`]
*   **`CRITICALITY_DIST`**:
    *   `'high'`: [Provide a probability, e.g., `0.40`]
    *   `'medium'`: [Provide a probability, e.g., `0.50`]
    *   `'low'`: [Provide a probability, e.g., `0.10`]
*   **`SCENARIO_MODIFIER`**: [Choose one: `0.5` (Dispersed), `1.0` (Point Failure), `1.5` (Strategic Priority)]
*   **`TECH_DEPENDENCY_MODIFIER`**: [Choose one: `0.25` (High), `1.0` (Low)]
*   **`POLITICAL_WILL_MODIFIER`**: [Choose one: `1.0` (Medium), `2.0` (High)]
*   **`HUMAN_CAPITAL_MODIFIER`**: [Choose one: `0.25` (High Impact), `1.0` (Low Impact)]

---

### **Part 2: Weekly Intelligence Summary & Justification**

*Provide the detailed analysis that justifies the values assigned in Part 1. Cite key assertions with sources.*
...
