import pandas as pd
import random

class CreativeGenerator:
    """
    Generates new creative ideas for low-performing ads.
    Uses dataset's existing creative messages to create variations.
    """

    def generate(self, df: pd.DataFrame):
        """
        Returns a list of creative recommendations for low-CTR ads.
        """

        avg_ctr = df["ctr"].mean()

        # Filter low-performing ads
        low_ctr_ads = df[df["ctr"] < avg_ctr].sort_values("ctr").head(5)

        recommendations = []

        for _, row in low_ctr_ads.iterrows():

            original = row["creative_message"]

            # Generate variations
            improved_headline = self.generate_headline(original)
            improved_message = self.generate_message(original)
            improved_cta = self.generate_cta()

            recommendations.append({
                "campaign_name": row["campaign_name"],
                "adset_name": row["adset_name"],
                "original_message": original,
                "new_headline": improved_headline,
                "new_message": improved_message,
                "new_cta": improved_cta,
                "ctr": float(row["ctr"])
            })

        return recommendations


    # -------------------------
    # Helper functions
    # -------------------------

    def generate_headline(self, text):
        templates = [
            "Experience the Difference: {}",
            "Why Customers Love This: {}",
            "Discover a Better Way: {}",
            "You Deserve Better: {}",
            "Upgrade Your Comfort With {}"
        ]
        return random.choice(templates).format(text.split(" ")[0].capitalize())


    def generate_message(self, text):
        templates = [
            "Introducing a fresh twist on {} — designed to improve comfort and confidence.",
            "Say goodbye to old styles. {} now comes with improved quality.",
            "Our customers asked for better, so we upgraded {} completely.",
            "Feel the comfort of {} like never before.",
            "{} just got better — perfect for everyday use."
        ]
        return random.choice(templates).format(text.capitalize())


    def generate_cta(self):
        ctas = [
            "Shop Now",
            "Learn More",
            "Try Today",
            "Discover More",
            "Buy Now",
            "Get Yours Today"
        ]
        return random.choice(ctas)
