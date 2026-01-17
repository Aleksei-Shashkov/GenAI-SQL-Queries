import sqlite3
DB_PATH = "nhl_stat.db"
def execute_sql(sql: str):  # Executes a SELECT SQL query against the SQLite database
                            # and returns the results as a list of dictionaries.
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute(sql)
    rows = cursor.fetchall()

    conn.close()

    return [dict(row) for row in rows]