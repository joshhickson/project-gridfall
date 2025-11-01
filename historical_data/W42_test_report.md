### **Refined HISTORICAL Intelligence Prompt for Project-Gridfall**

**Role:** You are a senior open-source intelligence (OSINT) analyst specializing in the Russian energy sector and its intersection with military-industrial capacity.

**Objective:** Your task is to provide a HISTORICAL intelligence report for a specific past week. The output of this report will be ingested by the `ingest_report.py` script to build the historical dataset for back-testing.

**Required Output Format:**

---

### **Part 0: Metadata**

*   **`period_id`**: [`2025-W42`]

---

### **Part 1: Simulator Input Variables (for `config.py`)**

*Provide the specific values for each variable based on your analysis for the reporting period.*

*   **`AVG_STRIKES_PER_WEEK`**: [`6.0`]
*   **`CRITICALITY_DIST`**:
    *   `'high'`: [`0.25`]
    *   `'medium'`: [`0.60`]
    *   `'low'`: [`0.15`]
*   **`SCENARIO_MODIFIER`**: [`1.0`]
*   **`TECH_DEPENDENCY_MODIFIER`**: [`1.0`]
*   **`POLITICAL_WILL_MODIFIER`**: [`1.0`]
*   **`HUMAN_CAPITAL_MODIFIER`**: [`1.0`]

---

### **Part 2: Weekly Intelligence Summary & Justification**

*This is a sample report for testing. A full report would contain detailed justification.*
