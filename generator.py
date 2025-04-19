from langchain_community.llms import Ollama
from utils.prompt_builder import build_prompt

def generate_tweets(config):
    model_name = config["model"]["name"]
    num_drafts = config["generation"].get("num_drafts", 3)

    llm = Ollama(model=model_name)
    prompt = build_prompt(num=num_drafts)
    output = llm.invoke(prompt)

    return [line.strip("-• ") for line in output.split("\n") if line.strip()]