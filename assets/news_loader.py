import json
from datetime import datetime
from pathlib import Path

def load_news():
    # Projekt-Root finden (Ordner von streamlitapp.py)
    project_root = Path(__file__).resolve().parent.parent

    # news.json im Hauptordner
    json_path = project_root / "news.json"

    if not json_path.exists():
        raise FileNotFoundError(f"news.json not found at: {json_path}")

    with open(json_path, "r", encoding="utf-8") as f:
        news = json.load(f)

    # Datum konvertieren
    for item in news:
        item["date"] = datetime.strptime(item["date"], "%Y-%m-%d")

    return news