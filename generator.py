from langchain_community.llms import Ollama
from fetcher import load_quarterly_data
import json
from pathlib import Path
import pandas as pd
import datetime
# ─── Load environment variables ─────────────────────────

# Utility to read and format markdown template
def read_markdown_template(file_path: str, **kwargs) -> str:
    """Load a markdown template and format it with provided keyword arguments."""
    template_path = Path(file_path)
    if not template_path.exists():
        raise FileNotFoundError(f"Markdown template not found: {file_path}")
    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()
    return template.format(**kwargs)

def df_to_serializable_json(df):
    return json.dumps(
        df.applymap(lambda x: x.isoformat() if isinstance(x, (pd.Timestamp, datetime.datetime)) else x)
          .to_dict(orient="records"),
        indent=2
    )

def generate_tweets(model_name="qwen3:8b", temperature=0.8, top_p=0.9, num_drafts=3):
    # ─── Load and convert CSV context ─────────────────────
    content_df, overview_df = load_quarterly_data()
    content_json = df_to_serializable_json(content_df)
    overview_json = df_to_serializable_json(overview_df)

    # ─── Build DeepThot system prompt from Markdown ───────
    system_prompt = read_markdown_template(
        "prompts/deepthot.md",
        topic = "",
        num_drafts=num_drafts,
        overview_json=overview_json,
        content_json=content_json
    )

    # ─── LLM Initialization ───────────────────────────────
    llm = Ollama(model=model_name, temperature=temperature, top_p=top_p)

    # ─── Generate Tweets ─────────────────────────────────
    response = llm.invoke(system_prompt)

    # ─── Normalize response ──────────────────────────────
    if hasattr(response, "generations"):
        text = response.generations[0][0].text
    elif isinstance(response, dict) and "response" in response:
        text = response["response"]
    else:
        text = str(response)

    drafts = [line.strip("‑• ") for line in text.split("\n") if line.strip()]
    return drafts
   