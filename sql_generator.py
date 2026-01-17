import json
from prompts import SQL_PROMPT_TEMPLATE
from sql_validator import validate_sql

def generate_sql(question: str, schema: dict, model) -> str:
    prompt = SQL_PROMPT_TEMPLATE.format(
        schema=json.dumps(schema, indent=2),
        question=question
    )
    response = model.generate_content(prompt)
    sql = response.text.strip()
    sql = sql.replace("```sql", "").replace("```", "").strip() # Убираем возможные sql-блоки
    validate_sql(sql)
    return sql
print("sql_generator loaded")
print(dir())