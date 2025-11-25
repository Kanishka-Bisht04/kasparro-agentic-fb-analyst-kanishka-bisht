import pandas as pd
import yaml
import os


class DataAgent:
    """
    Loads and summarizes the dataset.
    """

    def __init__(self):
        with open("config/config.yaml", "r") as f:
            config = yaml.safe_load(f)

        self.data_path = config["data_path"]

    def load_data(self):
        """
        Loads the CSV file into a DataFrame.
        """
        if not os.path.exists(self.data_path):
            raise FileNotFoundError(f"Dataset not found at {self.data_path}")

        df = pd.read_csv(self.data_path)
        return df

    def preprocess(self, df):
        """
        Cleans date + fills missing values.
        """
        if "date" in df.columns:
            df["date"] = pd.to_datetime(df["date"], errors="coerce")

        numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns
        df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())

        return df

    def summarize(self, df):
        """
        Creates summary dictionary.
        """

        summary = {
            "overall": {
                "total_spend": float(df["spend"].sum()),
                "total_impressions": int(df["impressions"].sum()),
                "total_clicks": int(df["clicks"].sum()),
                "total_revenue": float(df["revenue"].sum()),
                "avg_ctr": float(df["ctr"].mean()),
                "avg_roas": float(df["roas"].mean())
            },

            "campaign_summary": df.groupby("campaign_name")[
                ["spend", "impressions", "clicks", "revenue", "ctr", "roas"]
            ].mean().reset_index().to_dict(orient="records"),

            "low_ctr_ads": df[
                df["ctr"] < df["ctr"].mean()
            ].sort_values("ctr").head(5)[
                ["campaign_name", "adset_name", "creative_message", "ctr"]
            ].to_dict(orient="records")
        }

        return summary

    def load_and_summarize(self):
        df = self.load_data()
        df = self.preprocess(df)
        summary = self.summarize(df)
        return df, summary
