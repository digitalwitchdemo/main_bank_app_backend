import os
import pandas as pd
import psycopg2
from psycopg2.extras import execute_values

# Read CSV into DataFrame
df = pd.read_csv("dependency-check-report.csv")

# Optional: Convert ScanDate to proper timestamp
df["ScanDate"] = pd.to_datetime(df["ScanDate"], errors="coerce")

# Connect to PostgreSQL
conn = psycopg2.connect(
    host=os.environ["PG_HOST"],
    port=os.environ.get("PG_PORT", 5432),
    dbname=os.environ["PG_DATABASE"],
    user=os.environ["PG_USER"],
    password=os.environ["PG_PASSWORD"]
)
cur = conn.cursor()

# Insert data
columns = list(df.columns)
values = [tuple(x) for x in df.to_numpy()]

insert_query = f"""
    INSERT INTO owasp_dependency_report ({', '.join(columns)})
    VALUES %s
"""

execute_values(cur, insert_query, values)
conn.commit()

print(f"Inserted {len(values)} records.")
cur.close()
conn.close()
