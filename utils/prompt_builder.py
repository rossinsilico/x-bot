import yaml
import os

def build_prompt(topic: str = None, num: int = 3) -> str:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.abspath(os.path.join(base_dir, ".."))

    # Load persona metadata
    with open(os.path.join(root_dir, "prompts", "persona.yaml"), "r") as f:
        persona = yaml.safe_load(f)

    # Load prompt template
    with open(os.path.join(root_dir, "prompts", "base_template.txt"), "r") as f:
        template = f.read()

    # Use default topic if none is provided
    topic = topic or persona.get("default_topic", "technology")

    # Few-shot examples (optional, placeholder for now)
    examples = ""

    prompt = template.format(
        persona_voice=persona["voice"],
        persona_tone=persona["tone"],
        topic=topic,
        num=num,
        style_guide=persona["style_guide"],
        examples=examples
    )

    return prompt
