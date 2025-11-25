# Agent Architecture Diagram – Kasparro Agentic FB Analyst

User Query → Planner Agent
              ↓
        Data Agent → Dataset (CSV)
              ↓
        Insight Agent
              ↓
        Evaluator Agent
              ↓
   ┌───────────────────────┐
   │ Creative Generator     │
   └───────────────────────┘
              ↓
    Reports (insights.json, creatives.json, report.md)

Pipeline Flow:
1. Planner decomposes user query.
2. Data Agent loads + summarizes dataset.
3. Insight Agent generates hypotheses.
4. Evaluator validates hypotheses quantitatively.
5. Creative Generator proposes improved ad creatives.
6. Orchestrator stitches everything into a full pipeline.
7. run.py acts as CLI entry point.
