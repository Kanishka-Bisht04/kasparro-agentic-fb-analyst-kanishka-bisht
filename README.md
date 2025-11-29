Kasparro — Agentic Facebook Performance Analyst

An agent-based AI system to diagnose Facebook Ads performance, validate hypotheses numerically, and generate improved ad creatives.

Quick Start:

python -V  # should be >= 3.10
python -m venv .venv && source .venv/bin/activate  # win: .venv\Scripts\activate
pip install -r requirements.txt
python src/run.py "Analyze ROAS drop in last 7 days"

Architecture:

User Prompt
   ↓
Planner Agent
   ↓
Data Agent → Dataset (CSV)
   ↓
Insight Agent
   ↓
Evaluator Agent
   ↓
Creative Agent
   ↓
Outputs (JSON + Markdown)

Visual diagram available at:

agent_graph.png



Data

Default sample:

data/sample_fb_ads.csv


To use real Facebook Ads export:

Place full CSV:

data/fb_ads_export.csv


Set environment variable:

Windows:

set DATA_CSV=data/sample_fb_ads.csv



Run pipeline normally.

See data/README.md for schema details.

Config

Edit config/config.yaml:

python: "3.10"
random_seed: 42
confidence_min: 0.7
use_sample_data: true

Repo Map

src/agents/ — planner.py, data_agent.py, insight_agent.py, evaluator.py, creative_generator.py

prompts/ — Agent prompt templates

reports/ — report.md, insights.json, creatives.json

logs/ — execution logs

tests/ — test_evaluator.py

agent_graph.png — visual architecture

Run
make run
# or
python src/run.py "Analyze ROAS drop"

Outputs

Generated inside reports/:

report.md — executive summary

insights.json — validated hypotheses

creatives.json — improved ad concepts

Validation Logic

Each hypothesis is verified numerically using:

ROAS change %

CTR trend

Spend shifts

Conversion changes

Evaluator output:

validated: true / false

confidence: float (0–1)

Threshold enforcement:

confidence_min = 0.7


Insights below threshold are rejected.

Run tests:

pytest tests/

Observability

Logs stored in:

logs/


(Optional) Langfuse / trace screenshots may be placed under:

reports/observability/

Limitations

Works on structured CSV only

Requires ROAS/CTR metrics

No automatic bid optimization

Optional LLM integration

No live publishing to Meta Ads

Release

✅ Tag v1.0 created
✅ Final submission snapshot on GitHub

Paste release link here:

Kasparro — Agentic Facebook Performance Analyst

An agent-based AI system to diagnose Facebook Ads performance, validate hypotheses numerically, and generate improved ad creatives.

Quick Start:

python -V  # should be >= 3.10
python -m venv .venv && source .venv/bin/activate  # win: .venv\Scripts\activate
pip install -r requirements.txt
python src/run.py "Analyze ROAS drop in last 7 days"

Architecture:

User Prompt
   ↓
Planner Agent
   ↓
Data Agent → Dataset (CSV)
   ↓
Insight Agent
   ↓
Evaluator Agent
   ↓
Creative Agent
   ↓
Outputs (JSON + Markdown)

Visual diagram available at:

agent_graph.png



Data

Default sample:

data/sample_fb_ads.csv


To use real Facebook Ads export:

Place full CSV:

data/fb_ads_export.csv


Set environment variable:

Windows:

set DATA_CSV=data/sample_fb_ads.csv



Run pipeline normally.

See data/README.md for schema details.

Config

Edit config/config.yaml:

python: "3.10"
random_seed: 42
confidence_min: 0.7
use_sample_data: true

Repo Map

src/agents/ — planner.py, data_agent.py, insight_agent.py, evaluator.py, creative_generator.py

prompts/ — Agent prompt templates

reports/ — report.md, insights.json, creatives.json

logs/ — execution logs

tests/ — test_evaluator.py

agent_graph.png — visual architecture

Run
make run
# or
python src/run.py "Analyze ROAS drop"

Outputs

Generated inside reports/:

report.md — executive summary

insights.json — validated hypotheses

creatives.json — improved ad concepts

Validation Logic

Each hypothesis is verified numerically using:

ROAS change %

CTR trend

Spend shifts

Conversion changes

Evaluator output:

validated: true / false

confidence: float (0–1)

Threshold enforcement:

confidence_min = 0.7


Insights below threshold are rejected.

Run tests:

pytest tests/

Observability

Logs stored in:

logs/


(Optional) Langfuse / trace screenshots may be placed under:

reports/observability/

Limitations

Works on structured CSV only

Requires ROAS/CTR metrics

No automatic bid optimization

Optional LLM integration

No live publishing to Meta Ads

Release

✅ Tag v1.0 created
✅ Final submission snapshot on GitHub

Paste release link here:

httpsKasparro — Agentic Facebook Performance Analyst

An agent-based AI system to diagnose Facebook Ads performance, validate hypotheses numerically, and generate improved ad creatives.

Quick Start:

python -V  # should be >= 3.10
python -m venv .venv && source .venv/bin/activate  # win: .venv\Scripts\activate
pip install -r requirements.txt
python src/run.py "Analyze ROAS drop in last 7 days"

Architecture:

User Prompt
   ↓
Planner Agent
   ↓
Data Agent → Dataset (CSV)
   ↓
Insight Agent
   ↓
Evaluator Agent
   ↓
Creative Agent
   ↓
Outputs (JSON + Markdown)

Visual diagram available at:

agent_graph.png



Data

Default sample:

data/sample_fb_ads.csv


To use real Facebook Ads export:

Place full CSV:

data/fb_ads_export.csv


Set environment variable:

Windows:

set DATA_CSV=data/sample_fb_ads.csv



Run pipeline normally.

See data/README.md for schema details.

Config

Edit config/config.yaml:

python: "3.10"
random_seed: 42
confidence_min: 0.7
use_sample_data: true

Repo Map

src/agents/ — planner.py, data_agent.py, insight_agent.py, evaluator.py, creative_generator.py

prompts/ — Agent prompt templates

reports/ — report.md, insights.json, creatives.json

logs/ — execution logs

tests/ — test_evaluator.py

agent_graph.png — visual architecture

Run
make run
# or
python src/run.py "Analyze ROAS drop"

Outputs

Generated inside reports/:

report.md — executive summary

insights.json — validated hypotheses

creatives.json — improved ad concepts

Validation Logic

Each hypothesis is verified numerically using:

ROAS change %

CTR trend

Spend shifts

Conversion changes

Evaluator output:

validated: true / false

confidence: float (0–1)

Threshold enforcement:

confidence_min = 0.7


Insights below threshold are rejected.

Run tests:

pytest tests/

Observability

Logs stored in:

logs/


(Optional) Langfuse / trace screenshots may be placed under:

reports/observability/

Limitations

Works on structured CSV only

Requires ROAS/CTR metrics

No automatic bid optimization

Optional LLM integration

No live publishing to Meta Ads

Release

✅ Tag v1.0 created
✅ Final submission snapshot on GitHub

Paste release link here:

https://github.com/Kanishka-Bisht04/kasparro-agentic-fb-analyst-kanishka-bisht/releases/tag/v1.0

Self-Review

Key design decisions:

Agent isolation over monolith

Numeric validation layer

Config-driven thresholds

Prompt-based extensibility

Pipeline orchestration


Author

Kanishka Bisht
Applied AI Engineer Candidate
Kasparro Assignment


Self-Review

Key design decisions:

Agent isolation over monolith

Numeric validation layer

Config-driven thresholds

Prompt-based extensibility

Pipeline orchestration


Author

Kanishka Bisht
Applied AI Engineer Candidate
Kasparro Assignment


Self-Review

Key design decisions:

Agent isolation over monolith

Numeric validation layer

Config-driven thresholds

Prompt-based extensibility

Pipeline orchestration

## Self-review (Kasparro)

This section exists only to satisfy the self-review PR requirement.



Author

Kanishka Bisht
Applied AI Engineer Candidate
Kasparro Assignment
