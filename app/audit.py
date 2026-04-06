from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent.parent
LOG_FILE = BASE_DIR / "audit.log"


def log_event(username, action, status):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp} | user={username} | action={action} | status={status}\n"

    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(log_entry)
