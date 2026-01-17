SQL_PROMPT_TEMPLATE = """
You are given a SQLite database schema in JSON format.
You must generate a syntactically correct SQLite SQL query.

RULES:
- Use ONLY the tables and columns listed in the schema.
- Generate ONLY a single SELECT query.
- DO NOT use INSERT, UPDATE, DELETE, DROP, ALTER, or CREATE.
- DO NOT add explanations or comments.
- DO NOT use markdown.
- Return ONLY the SQL query as plain text.

Database schema:
{schema}

User question:
{question}

SQL query:
"""