import psycopg2
from pathlib import Path

conn = psycopg2.connect(
    dbname="healthcare_readmission",
    user="mona"
)

cur = conn.cursor()

schema_path = Path(__file__).resolve().parents[1] / "sql" / "schema.sql"

#"r opens the file in read mode, and f is the file handle used to read its contents. Using with ensures the file is automatically closed, which prevents resource leaks and makes the script safe and reproducible
with open(schema_path, "r") as f:
    schema_sql = f.read()

cur.execute(schema_sql)
conn.commit()

print("Schema successfully applied to database.")

cur.close()
conn.close()
