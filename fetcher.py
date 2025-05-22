import glob, os
import pandas as pd

DATA_DIR = os.path.join(os.path.dirname(__file__), "data/quarterly")

def _latest(pattern):
    files = sorted(glob.glob(os.path.join(DATA_DIR, pattern)))
    if not files:
        raise FileNotFoundError(f"No files match {pattern}")
    return files[-1]

def load_quarterly_data():
    # pick up the latest content & overview CSVs
    content_path  = _latest("*content*.csv")
    overview_path = _latest("*overview*.csv")

    # load with date parsing
    content_df  = pd.read_csv(content_path, parse_dates=["Date"])
    overview_df = pd.read_csv(overview_path, parse_dates=["Date"])

    print(f"🔍 Loaded content:  {content_path}")
    print(f"🔍 Loaded overview: {overview_path}")
    return content_df, overview_df

if __name__ == "__main__":
    content_df, overview_df = load_quarterly_data()
    # (Optional) save cleaned versions or summaries:
    content_df.to_json("data/quarterly/latest_content.json", orient="records", date_format="iso")
    overview_df.to_json("data/quarterly/latest_overview.json", orient="records", date_format="iso")
    print("✅ Quarterly data ingested.")