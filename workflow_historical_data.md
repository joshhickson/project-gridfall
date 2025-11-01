# OSINT Workflow for Historical Data Collection
**Document Date:** 2025-10-31
**Standard Timezone:** UTC (Coordinated Universal Time)

---

### **Objective**

The goal of this workflow is to systematically collect historical intelligence data to be used for back-testing and calibrating the Project-Gridfall simulator. This process involves creating a series of Markdown files, one for each historical week, which will then be automatically ingested by the system.

---

### **Step-by-Step Instructions**

**1. Define the Reporting Period**
*   For each historical week you analyze, define a precise 7-day period.
*   The start and end dates must be in `YYYY-MM-DD` format and will represent the UTC date. A standard week runs from Monday to Sunday.
*   **Example:** `2025-10-20` to `2025-10-26`.

**2. Create a New Report File**
*   Create a new Markdown file (`.md`) for the defined period.
*   **Location:** Place all new report files in the `historical_data/` directory.
*   **Naming Convention:** Use the start date for the filename to ensure chronological order.
    *   **Example:** `2025-10-20_report.md`

**3. Populate the Report**
*   Copy the entire contents of the `prompt_template_historical.md` file into your new report file.
*   Fill out all the required fields based on your OSINT research for that specific 7-day UTC period.

**4. Verify Machine-Readability (Critical Checklist)**
*   Before finalizing a report, ensure it can be read by the automated `ingest_report.py` script by checking the following in the "Part 1" section:
    *   **`start_date_utc` / `end_date_utc`**: Ensure both dates are present and in `YYYY-MM-DD` format within the brackets.
    *   **Numerical Variables**: For fields like `AVG_STRIKES_PER_WEEK`, ensure there is a single, clean number inside the brackets (e.g., `[6.0]`, not `[approx. 6]`).
    *   **`CRITICALITY_DIST`**: Ensure each of the `'high'`, `'medium'`, and `'low'` lines has its own numerical probability in brackets.

**5. Notify for Ingestion**
*   Once you have one or more completed and verified report files in the `historical_data/` directory, simply notify me.
*   **Example:** "The reports for October are ready for ingestion."
*   I will then execute the ingestion script to automatically process the files and will provide you with a confirmation.
