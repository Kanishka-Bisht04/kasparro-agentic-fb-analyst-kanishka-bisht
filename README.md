Kasparro – Agentic Facebook Performance Analyst

This project implements an end-to-end multi-agent pipeline to analyze Facebook Ads performance (CTR, ROAS), explain performance drops, validate insights, and generate improved creative ideas.

-------------------------------------------------------
1. Overview
-------------------------------------------------------

The system uses the following agents:

1. Planner Agent – Breaks down the user query into clear steps.
2. Data Agent – Loads, cleans, and summarizes the dataset.
3. Insight Agent – Generates hypotheses about ROAS/CTR changes.
4. Evaluator Agent – Validates hypotheses using numeric checks.
5. Creative Generator – Creates improved creative ideas.
6. Orchestrator – Connects all agents into one pipeline.
7. run.py – Entry point for executing the pipeline.

A typical command such as:

python src/run.py "Analyze ROAS drop"

will produce three output files inside the reports/ folder:

- insights.json
- creatives.json
- report.md

-------------------------------------------------------
2. Project Structure
-------------------------------------------------------

kasparro-agentic-fb-analyst-kanishka-bisht/
│
├── config/
│   └── config.yaml
├── data/
│   └── sample_fb_ads.csv
├── logs/
├── prompts/
│   ├── planner_prompt.md
│   ├── data_agent_prompt.md
│   ├── insight_prompt.md
│   ├── evaluator_prompt.md
│   └── creative_prompt.md
├── reports/
│   ├── insights.json
│   ├── creatives.json
│   └── report.md
├── src/
│   ├── agents/
│   │   ├── planner.py
│   │   ├── data_agent.py
│   │   ├── insight_agent.py
│   │   ├── evaluator.py
│   │   └── creative_generator.py
│   ├── orchestrator.py
│   └── run.py
├── tests/
│   └── test_evaluator.py
└── README.md

-------------------------------------------------------
3. Setup Instructions
-------------------------------------------------------

Step 1: Create a virtual environment

python -m venv .venv

Activate (Windows):
.venv\Scripts\activate

Step 2: Install dependencies

pip install -r requirements.txt

-------------------------------------------------------
4. How to Run the Pipeline
-------------------------------------------------------

Run the full agentic pipeline using:

python src/run.py "Analyze ROAS drop"

This will generate the following output files:

- reports/insights.json
- reports/creatives.json
- reports/report.md

-------------------------------------------------------
5. Example Output (Plain Text)
-------------------------------------------------------

insights.json (example):

[
  {
    "hypothesis": "CTR is lower than benchmark.",
    "validated_truth": "True",
    "confidence": 0.78
  }
]

creatives.json (example):

[
  {
    "campaign_name": "Campaign A",
    "new_headline": "Experience the Difference",
    "new_message": "Introducing a refined version of the original creative.",
    "new_cta": "Shop Now"
  }
]

-------------------------------------------------------
6. Requirements
-------------------------------------------------------

- Python 3.10+
- pandas
- pyyaml
- json
- openai (if LLM extensions are added)

-------------------------------------------------------
7. Submission Checklist
-------------------------------------------------------

[ ] Correct folder structure  
[ ] insights.json generated  
[ ] creatives.json generated  
[ ] report.md generated  
[ ] README.md completed  
[ ] Code pushed to GitHub  
[ ] v1.0 release created  
[ ] Submitted via Google Form

-------------------------------------------------------
End of File
-------------------------------------------------------
