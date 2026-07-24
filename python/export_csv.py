"""
===============================================================================
Project : Data Foundations: SQL Extraction, Cleaning & Outlier Audit
Course  : Data Analytics with Gen & Agentic AI
Capstone: Part 1

File    : export_csv.py
Task    : Task 6 - Export JOIN Result to CSV

Objective:
Export the Task 4 JOIN result from MySQL into a CSV file. The exported dataset
will be used for:

1. Task 7 - Data Cleaning
2. Task 8 - Outlier Detection

Author  : Bhuvaneswari Yennapusala
===============================================================================
"""

# =============================================================================
# IMPORT REQUIRED LIBRARIES
# =============================================================================

import os
import pandas as pd
from sqlalchemy import create_engine

# =============================================================================
# DATABASE CONFIGURATION
# =============================================================================

HOST = "localhost"
PORT = 3306
USER = "root"
PASSWORD = ""          # XAMPP default password
DATABASE = "smartcommerce_analytics"

# =============================================================================
# CREATE DATABASE CONNECTION
# =============================================================================

print("=" * 70)
print("Connecting to MySQL Database...")
print("=" * 70)

try:
    engine = create_engine(
        f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
    )

    # =========================================================================
    # TASK 4 JOIN QUERY
    # =========================================================================
    # Purpose:
    # Export customer and order information for further preprocessing.
    #
    # INNER JOIN is used because only customers with matching orders are
    # required for cleaning and outlier analysis.
    # =========================================================================

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

    # =========================================================================
    # READ DATA FROM MYSQL
    # =========================================================================

    df = pd.read_sql(query, engine)

    # =========================================================================
    # CREATE OUTPUT DIRECTORY
    # =========================================================================

    project_root = os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )

    output_folder = os.path.join(project_root, "output", "reports")

    os.makedirs(output_folder, exist_ok=True)

    # =========================================================================
    # EXPORT CSV
    # =========================================================================

    output_file = os.path.join(
        output_folder,
        "orders_customers_join.csv"
    )

    df.to_csv(output_file, index=False)

    # =========================================================================
    # EXPORT SUMMARY
    # =========================================================================

    print("\n" + "=" * 70)
    print("TASK 6 COMPLETED SUCCESSFULLY")
    print("=" * 70)
    print(f"Rows Exported      : {len(df)}")
    print(f"Columns Exported   : {len(df.columns)}")
    print(f"CSV Location       : {output_file}")
    print("=" * 70)

except Exception as error:
    print("\nERROR OCCURRED")
    print("-" * 70)
    print(error)
    print("-" * 70)

finally:
    try:
        engine.dispose()
    except Exception:
        pass
    