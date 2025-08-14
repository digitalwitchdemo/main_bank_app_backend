  # - name: Set up Python
      #   uses: actions/setup-python@v5
      #   with:
      #     python-version: '3.11'

      # - name: Install dependencies
      #   run: |
      #     pip install pandas psycopg2-binary

      # - name: Import CSV to PostgreSQL
      #   env:
      #     PG_HOST: ${{ secrets.PG_HOST }}
      #     PG_PORT: ${{ secrets.PG_PORT }}
      #     PG_DATABASE: ${{ secrets.PG_DATABASE }}
      #     PG_USER: ${{ secrets.PG_USER }}
      #     PG_PASSWORD: ${{ secrets.PG_PASSWORD }}
      #   run: python import_owasp_to_postgres.py







import os
import pandas as pd
import psycopg2
from psycopg2.extras import execute_values

# Load CSV
csv_path = "./target/dependency-check-report.csv"
df = pd.read_csv(csv_path)

# Clean column names to match DB schema
rename_map = {
    "Project": "project",
    "ScanDate": "scan_date",
    "DependencyName": "dependency_name",
    "DependencyPath": "dependency_path",
    "Description": "description",
    "License": "license",
    "Md5": "md5",
    "Sha1": "sha1",
    "Identifiers": "identifiers",
    "CPE": "cpe",
    "CVE": "cve",
    "CWE": "cwe",
    "Vulnerability": "vulnerability",
    "Source": "source",
    "CVSSv2_Severity": "cvssv2_severity",
    "CVSSv2_Score": "cvssv2_score",
    "CVSSv2": "cvssv2",
    "CVSSv3_BaseSeverity": "cvssv3_base_severity",
    "CVSSv3_BaseScore": "cvssv3_base_score",
    "CVSSv3": "cvssv3",
    "CVSSv4_BaseSeverity": "cvssv4_base_severity",
    "CVSSv4_BaseScore": "cvssv4_base_score",
    "CVSSv4": "cvssv4",
    "CPE Confidence": "cpe_confidence",
    "Evidence Count": "evidence_count",
    "VendorProject": "vendor_project",
    "Product": "product",
    "Name": "name",
    "DateAdded": "date_added",
    "ShortDescription": "short_description",
    "RequiredAction": "required_action",
    "DueDate": "due_date",
    "Notes": "notes"
}

# Apply the renaming
df.rename(columns=rename_map, inplace=True)

# Ensure scan_date is datetime
if "scan_date" in df.columns:
    df["scan_date"] = pd.to_datetime(df["scan_date"], errors="coerce")


# Connect to PostgreSQL
conn = psycopg2.connect(
    host="18.206.246.139",
    port="5432",
    dbname="secopsdb",
    user="secops",
    password="supersecurepassword"
    
    # host=os.environ["PG_HOST"],
    # port=os.environ.get("PG_PORT", 5432),
    # dbname=os.environ["PG_DATABASE"],
    # user=os.environ["PG_USER"],
    # password=os.environ["PG_PASSWORD"]
)
cur = conn.cursor()

# Prepare insert
columns = list(df.columns)
values = [tuple(x) for x in df.to_numpy()]
insert_query = f"""
    INSERT INTO owasp_dependency_report ({', '.join(columns)})
    VALUES %s
"""

# Execute insert
execute_values(cur, insert_query, values)
conn.commit()
print(f"✅ Inserted {len(values)} rows.")

cur.close()
conn.close()
