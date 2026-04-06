import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
USERS_FILE = BASE_DIR / "sample_data" / "users.json"


def load_users():
    with open(USERS_FILE, "r", encoding="utf-8") as file:
        return json.load(file)
