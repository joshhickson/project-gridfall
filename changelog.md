2025-10-30 03:05:07
-------------------

*   Initial setup of the project structure, including `simulator.py`, `config.py`, `changelog.md`, and `README.md`.
*   Populated `config.py` with default values.
*   Implemented the core simulator logic in `simulator.py`.
2025-11-01 00:00 UTC
-------------------

*   **Upgraded Prompt Engineering:** Standardized all intelligence report prompts (`prompt_template.md`, `prompt_template_historical.md`, `daily_model/prompt_template_daily.md`) to a new, more sophisticated "master" template based on advanced prompt engineering principles (Persona, CoT, Few-Shot, RAG). This significantly increases the rigor and quality of our core data collection and analytical process.

2025-10-31 19:20 UTC
-------------------

*   **Standardized Historical Workflow:** Created `workflow_historical_data.md` to document the OSINT process for back-testing.
*   Created `prompt_template_historical.md`, a new prompt template that uses precise, machine-readable UTC date ranges instead of abstract week numbers to improve the data ingestion process.

***

2025-11-01 13:16 UTC
-------------------

*   **Created Data Collection Manifest:** To support a large-scale back-testing effort, a new, more organized data collection workflow has been established.
    *   Created `generate_manifest.py`, a script that programmatically generates a CSV (`historical_data_manifest.csv`) of all weekly periods required for the back-testing phases. This ensures data integrity and provides a clear tracking mechanism.
    *   Updated the `workflow_historical_data.md` to instruct analysts on how to use the new manifest-driven process.

***

*   Added the project brief to `README.md`.

***
