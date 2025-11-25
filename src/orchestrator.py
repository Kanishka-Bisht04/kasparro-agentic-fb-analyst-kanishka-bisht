import json
from agents.planner import PlannerAgent
from agents.data_agent import DataAgent
from agents.insight_agent import InsightAgent
from agents.evaluator import EvaluatorAgent
from agents.creative_generator import CreativeGenerator


class Orchestrator:
    """
    Main pipeline controller that connects all agents.
    """

    def __init__(self):
        self.planner = PlannerAgent()
        self.data_agent = DataAgent()
        self.insight_agent = InsightAgent()
        self.evaluator = EvaluatorAgent()
        self.creative_gen = CreativeGenerator()

    def run(self, query: str):

        # 1. Planner
        tasks = self.planner.plan(query)
        print("\n🔹 Planner Tasks:")
        for t in tasks:
            print(" -", t)

        # 2. Data
        df, summary = self.data_agent.load_and_summarize()
        print("\n🔹 Data Loaded & Summarized")

        # 3. Hypotheses
        hypotheses = self.insight_agent.generate(summary)
        print("\n🔹 Insight Hypotheses Generated:", len(hypotheses))

        # 4. Validation
        validated_insights = self.evaluator.validate(hypotheses, df)
        print("\n🔹 Insights Validated")

        # 5. Creative generation
        creative_recos = self.creative_gen.generate(df)
        print("\n🔹 Creative Suggestions Generated:", len(creative_recos))

        # -------------------------------------
        # FIX A: Convert bool → string for JSON
        # -------------------------------------
        cleaned_insights = []
        for item in validated_insights:
            clean = item.copy()
            clean["validated_truth"] = str(item["validated_truth"])
            cleaned_insights.append(clean)

        # -------------------------------------
        # FIX B: Write insights.json
        # -------------------------------------
        with open("reports/insights.json", "w", encoding="utf-8") as f:
            json.dump(cleaned_insights, f, indent=4, ensure_ascii=False)

        # -------------------------------------
        # FIX C: Write creatives.json
        # -------------------------------------
        with open("reports/creatives.json", "w", encoding="utf-8") as f:
            json.dump(creative_recos, f, indent=4, ensure_ascii=False)

        # -------------------------------------
        # FIX D: Unicode-safe report writing
        # -------------------------------------
        with open("reports/report.md", "w", encoding="utf-8") as f:
            f.write("# Marketing Performance Report\n\n")

            f.write("## Validated Insights\n\n")
            for i in cleaned_insights:
                f.write(f"- **{i['hypothesis']}**\n")
                f.write(f"  - Evidence: {i['evidence']}\n")
                f.write(f"  - Confidence: {i['confidence']}\n")
                f.write(f"  - Validated Truth: {i['validated_truth']}\n\n")

            f.write("\n## Creative Recommendations\n\n")
            for c in creative_recos:
                f.write(f"- **Campaign**: {c['campaign_name']}\n")
                f.write(f"  - Original: {c['original_message']}\n")
                f.write(f"  - New Headline: {c['new_headline']}\n")
                f.write(f"  - New Message: {c['new_message']}\n")
                f.write(f"  - CTA: {c['new_cta']}\n\n")

        print("\n✅ All outputs saved inside reports/ folder!")

        return {
            "tasks": tasks,
            "summary": summary,
            "validated_insights": cleaned_insights,
            "creative_recos": creative_recos
        }
