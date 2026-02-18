import psycopg2
from pathlib import Path

conn = psycopg2.connect(
    dbname="healthcare_readmission",
    user="mona"
)

cur = conn.cursor()

schema_path = Path(__file__).resolve().parents[1] / "sql" / "schema.sql"

with open(schema_path, "r") as f:
    schema_sql = f.read()

cur.execute(schema_sql)
conn.commit()

print("Schema successfully applied to database.")

cur.close()
conn.close()
