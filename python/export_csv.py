"""
===============================================================================
Project : Data Foundations: SQL Extraction, Cleaning & Outlier Audit
Course  : Data Analytics with Gen & Agentic AI
Capstone: Part 1

File    : export_csv.py

Description:
Exports the Task 4 INNER JOIN result from MySQL into a CSV file
for further cleaning and outlier analysis.

Author  : Bhuvaneswari Yennapusala
===============================================================================
"""

import os
import pandas as pd
from sqlalchemy import create_engine

# =============================================================================
# Database Configuration
# =============================================================================

HOST = "localhost"
PORT = 3306
USER = "root"
PASSWORD = ""          # Default XAMPP password is blank
DATABASE = "smartcommerce_analytics"

# =============================================================================
# Create MySQL Connection
# =============================================================================

engine = create_engine(
    f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
)

# =============================================================================
# SQL Query (Task 4 INNER JOIN)
# =============================================================================

query = """
SELECT
    c.customer_id,
    c.customer_city,
    c.customer_state,
    o.order_id,
    o.order_status,
    o.order_purchase_timestamp
FROM customers AS c
INNER JOIN orders AS o
ON c.customer_id = o.customer_id;
"""

# =============================================================================
# Read Data from MySQL
# =============================================================================

print("Connecting to MySQL...")
df = pd.read_sql(query, engine)

# =============================================================================
# Create Output Folder Automatically
# =============================================================================

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

output_folder = os.path.join(project_root, "output", "reports")

os.makedirs(output_folder, exist_ok=True)

# =============================================================================
# Export CSV
# =============================================================================

output_file = os.path.join(output_folder, "orders_customers_join.csv")

df.to_csv(output_file, index=False)

# =============================================================================
# Success Message
# =============================================================================

print("\n" + "=" * 65)
print("CSV EXPORTED SUCCESSFULLY")
print("=" * 65)
print(f"Rows Exported   : {len(df)}")
print(f"Columns Exported: {len(df.columns)}")
print(f"Output Folder   : {output_folder}")
print(f"CSV File        : {output_file}")
print("=" * 65)