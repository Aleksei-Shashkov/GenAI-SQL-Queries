import sqlite3
import json

DB_PATH = "nhl_stat.db"
OUTPUT_FILE = "schema.json"

def explore_schema(db_path: str) -> dict:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    schema = {
        "database": db_path,
        "tables": {}
    }

    # Получаем список таблиц
    cursor.execute("""
        SELECT name FROM sqlite_master
        WHERE type='table' AND name NOT LIKE 'sqlite_%';
    """)
    tables = [row[0] for row in cursor.fetchall()]

    for table in tables:
        cursor.execute(f"PRAGMA table_info({table});")
        columns = cursor.fetchall()

        schema["tables"][table] = {
            "columns": [
                {"name": col[1],"type": col[2]}
                for col in columns
            ]
        }

    conn.close()
    return schema

def save_schema(schema: dict, output_file: str):
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(schema, f, indent=2)

if __name__ == "__main__":
    schema = explore_schema(DB_PATH)
    save_schema(schema, OUTPUT_FILE)
    print(f"Schema saved to {OUTPUT_FILE}")