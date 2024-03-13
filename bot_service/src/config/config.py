import os
import yaml
from dotenv import load_dotenv

load_dotenv()

CONFIG_PATH = "src/config/config.yaml"

BOT_TOKEN = os.getenv("BOT_TOKEN")


with open(CONFIG_PATH, "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)
    welcome_message = config["messages"]["welcome"]