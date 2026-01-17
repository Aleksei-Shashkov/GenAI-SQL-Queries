import re

FORBIDDEN_SQL = re.compile(
    r"\b(INSERT|UPDATE|DELETE|DROP|ALTER|CREATE|TRUNCATE)\b",
    re.IGNORECASE
)

def validate_sql(sql: str):
    if FORBIDDEN_SQL.search(sql):
        raise ValueError("Forbidden SQL operation detected.")

    if not sql.lower().startswith("select"):
        raise ValueError("Only SELECT queries are allowed.")