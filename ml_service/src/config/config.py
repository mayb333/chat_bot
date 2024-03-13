import yaml

CONFIG_PATH = "src/config/config.yaml"

with open(CONFIG_PATH, "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)
    PROMPT_TEMPLATE = config["prompts"]["model_prompt"]
