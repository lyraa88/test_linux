import os
import requests
import json
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

TMP_DIR = "/tmp"
TMP_FILE = os.path.join(TMP_DIR, "test.json")

def main():
    current_minute = datetime.now().minute
    target_id = (current_minute + 1) % 60

    url = f"https://jsonplaceholder.typicode.com/todos/{target_id}"
    print(f"[INFO] Fetching from: {url}")
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    os.makedirs(TMP_DIR, exist_ok=True)

    with open(TMP_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"[INFO] Saved data to {TMP_FILE}")

if __name__ == "__main__":
    main()
