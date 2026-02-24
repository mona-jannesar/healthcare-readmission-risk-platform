#I use psycopg2 to manage database connections and cursors. I execute schema SQL programmatically to make database setup reproducible. For loading data, I batch-insert cleaned CSVs using parameterized queries and commit transactions explicitly. After loading, I validate row counts and foreign key consistency to ensure data integrity before modeling.

import pandas as pd
import psycopg2 
from psycopg2.extras import execute_batch #efficiently insert many rows (much faster than one-by-one)
#This script uses psycopg2.extras.execute_batch for faster inserts — a good practice for large datasets.
from pathlib import Path

DBNAME = "healthcare_readmission"
USER = "mona"

def connect():
    return psycopg2.connect(
        dbname=DBNAME,
        user=USER
    )

def truncate_tables():
    conn = connect()
    cur = conn.cursor()

    # 🔎 DEBUG: prove which DB and user we are connected to
    cur.execute("SELECT current_database(), current_user;")
    print("Connected to:", cur.fetchone())

    # Order matters because of foreign keys
    cur.execute("TRUNCATE TABLE outcomes, diagnoses, encounters, patients RESTART IDENTITY CASCADE;")
    conn.commit()
    cur.close()
    conn.close()
    print("Tables truncated.")

def load_table(csv_path, table_name, columns):
    df = pd.read_csv(csv_path, dtype=str)  # Read all data as strings to avoid type issues
    df = df.where(pd.notnull(df), None)  # <-- convert NaN to None for SQL NULL

    conn = connect()
    cur = conn.cursor()

   # Build parameterized insert statement
    placeholders = ", ".join(["%s"] * len(columns))
    cols = ", ".join(columns)

    query = f"INSERT INTO {table_name} ({cols}) VALUES ({placeholders})"

    data = df[columns].values.tolist()
    execute_batch(cur, query, data)

    conn.commit()

    # Check rows loaded
    cur.execute(f"SELECT COUNT(*) FROM {table_name}")
    count = cur.fetchone()[0]
    print(f"{table_name}: {count:,} rows")

    cur.close()
    conn.close()

if __name__ == "__main__":
    # Reset tables so script is safe to re-run during development
    truncate_tables()

    load_table("data/processed/patients.csv", "patients", ["patient_id", "gender", "age_group", "race"])
    load_table("data/processed/encounters.csv", "encounters", [
            "encounter_id",
            "patient_id",
            "admission_type",
            "discharge_disposition",
            "admission_source",
            "time_in_hospital",
            "num_lab_procedures",
            "num_medications",
            "readmitted"
        ])
    
    load_table("data/processed/outcomes.csv", "outcomes",
        ["encounter_id", "readmission_30day", "readmission_90day"]
    )