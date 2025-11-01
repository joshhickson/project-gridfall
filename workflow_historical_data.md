# OSINT Workflow for Historical Data Collection
**Document Date:** 2025-11-01
**Standard Timezone:** UTC (Coordinated Universal Time)

---

### **Objective**

The goal of this workflow is to systematically collect historical intelligence data to be used for back-testing and calibrating the Project-Gridfall simulator. This process is managed by the `historical_data_manifest.csv` file.

---

### **Step-by-Step Instructions**

**1. Consult the Manifest**
*   Open the `historical_data_manifest.csv` file.
*   Find a row with the `status` of "Pending". This is your next task.
*   The manifest provides the precise `start_date_utc`, `end_date_utc`, and the exact `report_filename` you will need to create.

**2. Create the Report File**
*   Create a new Markdown file (`.md`) in the `historical_data/` directory with the exact filename specified in the manifest.
*   **Example:** `historical_data/2025-07-28_report.md`

**3. Populate the Report**
*   Copy the entire contents of the `prompt_template_historical.md` file into your new report file.
*   Fill out all the required fields based on your OSINT research for the 7-day UTC period defined in the manifest.

**4. Verify Machine-Readability (Critical Checklist)**
*   Before finalizing, ensure the report can be read by the automated `ingest_report.py` script by checking the following in the "Part 0" and "Part 1" sections:
    *   **`start_date_utc` / `end_date_utc`**: Ensure the dates in the report match the dates in the manifest.
    *   **Numerical Variables**: Ensure all fields like `AVG_STRIKES_PER_WEEK` contain a single, clean number inside the brackets (e.g., `[6.0]`).
    *   **`CRITICALITY_DIST`**: Ensure `'high'`, `'medium'`, and `'low'` each have their own numerical probability in brackets.

**5. Notify for Ingestion**
*   Once you have completed and verified one or more report files, simply notify me.
*   **Example:** "The reports for July and August are ready for ingestion."
*   I will then execute the ingestion script, which will automatically update the status of the corresponding rows in the manifest to "Ingested" upon successful processing.
