"""
Project : Data Foundations: SQL Extraction, Cleaning & Outlier Audit
Course  : Data Analytics with Gen & Agentic AI
Capstone: Part 1

File    : export_csv.py
Task    : Task 6 - Export JOIN Result to CSV

Objective:
Export the Task 4 JOIN result from MySQL into a CSV file.

The exported CSV will be used for:
1. Task 7 - Data Cleaning
2. Task 8 - Outlier Detection

Author  : Bhuvaneswari Yennapusala
"""

# ============================================================================
# IMPORT REQUIRED LIBRARIES
# ============================================================================

import os
import pandas as pd
from sqlalchemy import create_engine


# ============================================================================
# DATABASE CONFIGURATION
# ============================================================================

HOST = "localhost"
PORT = 3306
USER = "root"
PASSWORD = ""          # XAMPP default MySQL/MariaDB password
DATABASE = "smartcommerce_analytics"


# ============================================================================
# DATABASE CONNECTION
# ============================================================================

print("=" * 70)
print("Connecting to MySQL/MariaDB Database...")
print("=" * 70)

engine = None

try:

    engine = create_engine(
        f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
    )

    # ========================================================================
    # TASK 4 JOIN QUERY
    # ========================================================================
    # Purpose:
    # Export the INNER JOIN result from Task 4.
    #
    # INNER JOIN is used because Task 4 requires customers having
    # matching orders.
    # ========================================================================

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
        ON c.customer_id = o.customer_id
    ORDER BY o.order_id ASC;
    """

    # ========================================================================
    # READ JOIN RESULT FROM DATABASE
    # ========================================================================

    print("\nReading Task 4 JOIN result from database...")

    df = pd.read_sql(query, engine)

    print("JOIN query executed successfully.")


    # ========================================================================
    # CREATE OUTPUT DIRECTORY
    # ========================================================================

    # Assumes this file is located inside a scripts/ folder.
    # Example:
    #
    # project/
    # ├── scripts/
    # │   └── export_csv.py
    # └── output/
    #     └── reports/

    project_root = os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )

    output_folder = os.path.join(
        project_root,
        "output",
        "reports"
    )

    os.makedirs(output_folder, exist_ok=True)


    # ========================================================================
    # EXPORT JOIN RESULT TO CSV
    # ========================================================================

    output_file = os.path.join(
        output_folder,
        "orders_customers_join.csv"
    )

    df.to_csv(
        output_file,
        index=False
    )


    # ========================================================================
    # VERIFY CSV
    # ========================================================================

    file_exists = os.path.exists(output_file)

    # ========================================================================
    # TASK 6 SUMMARY
    # ========================================================================

    print("\n" + "=" * 70)
    print("TASK 6 - CSV EXPORT COMPLETED SUCCESSFULLY")
    print("=" * 70)

    print(f"Rows Exported    : {len(df)}")
    print(f"Columns Exported : {len(df.columns)}")
    print(f"CSV Created      : {file_exists}")
    print(f"CSV Location     : {output_file}")

    print("\nColumns exported:")

    for column in df.columns:
        print(f"  - {column}")

    print("=" * 70)


# ============================================================================
# ERROR HANDLING
# ============================================================================

except Exception as error:

    print("\n" + "=" * 70)
    print("TASK 6 FAILED")
    print("=" * 70)

    print("Error:")
    print(error)

    print("=" * 70)


# ============================================================================
# CLOSE DATABASE CONNECTION
# ============================================================================

finally:

    if engine is not None:
        engine.dispose()

        print("\nDatabase connection closed.")