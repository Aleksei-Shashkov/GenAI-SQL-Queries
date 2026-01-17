import json
def load_schema(path: str) -> dict: # Loads database schema from a JSON file.
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)