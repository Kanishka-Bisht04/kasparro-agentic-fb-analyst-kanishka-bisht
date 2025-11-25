class PlannerAgent:
    """
    The Planner Agent breaks the user query into clear steps.
    """

    def plan(self, query: str):
        tasks = [
            "Load the dataset",
            "Compute metrics (CTR, ROAS, Spend, Impressions, Revenue)",
            "Identify trends (7-day, 30-day)",
            "Detect performance drops",
            "Generate hypotheses explaining ROAS/CTR changes",
            "Validate hypotheses using quantitative checks",
            "Identify low-CTR campaigns",
            "Generate improved creative ideas",
            "Write insights.json",
            "Write creatives.json",
            "Write final report.md"
        ]

        return tasks
