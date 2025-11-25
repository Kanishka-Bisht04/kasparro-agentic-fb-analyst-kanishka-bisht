class InsightAgent:
    """
    The Insight Agent generates hypotheses about
    why ROAS or CTR changed based on summarized data.
    """

    def generate(self, summary: dict):
        """
        Creates a list of hypotheses with evidence.
        """

        insights = []

        overall = summary.get("overall", {})
        avg_ctr = overall.get("avg_ctr", 0)
        avg_roas = overall.get("avg_roas", 0)
        low_ctr_ads = summary.get("low_ctr_ads", [])
        campaign_summary = summary.get("campaign_summary", [])

        # -------------------------------------------------
        # 1. Hypothesis: CTR is below ideal benchmark
        # -------------------------------------------------
        if avg_ctr < 0.02:  # 2% CTR is a common benchmark
            insights.append({
                "hypothesis": "CTR is lower than expected. Possible creative fatigue or weak messaging.",
                "evidence": f"Average CTR = {avg_ctr:.3f}, which is below 2% benchmark.",
                "category": "ctr_issue"
            })

        # -------------------------------------------------
        # 2. Hypothesis: ROAS dropped
        # -------------------------------------------------
        if avg_roas < 1.0:
            insights.append({
                "hypothesis": "ROAS is below 1.0. Revenue < Spend. Possible poor targeting or high CPC.",
                "evidence": f"Average ROAS = {avg_roas:.2f}",
                "category": "roas_issue"
            })

        # -------------------------------------------------
        # 3. Hypothesis: Some creatives are failing
        # -------------------------------------------------
        if len(low_ctr_ads) > 0:
            insights.append({
                "hypothesis": "Some creatives are significantly underperforming, indicating potential messaging fatigue.",
                "evidence": low_ctr_ads,
                "category": "creative_fatigue"
            })

        # -------------------------------------------------
        # 4. Hypothesis: Certain campaigns have major performance gaps
        # -------------------------------------------------
        for camp in campaign_summary:
            try:
                if camp["roas"] < avg_roas * 0.8:  # 20% below average ROAS
                    insights.append({
                        "hypothesis": f"Campaign '{camp['campaign_name']}' is underperforming vs overall performance.",
                        "evidence": camp,
                        "category": "campaign_underperformance"
                    })
            except:
                pass

        return insights
