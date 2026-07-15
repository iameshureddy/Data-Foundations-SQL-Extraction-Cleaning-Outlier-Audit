"""
===============================================================================
Project : Data Foundations: SQL Extraction, Cleaning & Outlier Audit
Course  : Data Analytics with Gen & Agentic AI
Capstone: Part 1

File    : outlier_analysis.py

Author  : Bhuvaneswari Yennapusala

Description:
Detects outliers using both IQR and Z-Score methods and generates
a detailed report.
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
PASSWORD = ""
DATABASE = "smartcommerce_analytics"

engine = create_engine(
    f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
)

# =============================================================================
# Output Folder
# =============================================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

REPORT_FOLDER = os.path.join(BASE_DIR, "output", "reports")

os.makedirs(REPORT_FOLDER, exist_ok=True)

REPORT_FILE = os.path.join(
    REPORT_FOLDER,
    "outlier_analysis_report.txt"
)

# =============================================================================
# Load Data
# =============================================================================

query = """
SELECT
    price,
    freight_value
FROM order_items;
"""

print("Loading data from MySQL...")

df = pd.read_sql(query, engine)

print("Rows :", len(df))

# =============================================================================
# IQR Analysis
# =============================================================================

iqr_results = []

print("\n" + "=" * 60)
print("IQR METHOD")
print("=" * 60)

for column in df.columns:

    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)

    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    count = len(df[(df[column] < lower) | (df[column] > upper)])

    iqr_results.append((column, count))

    print(f"{column:<20} {count}")

# =============================================================================
# Z Score Analysis
# =============================================================================

zscore_results = []

print("\n" + "=" * 60)
print("Z-SCORE METHOD")
print("=" * 60)

for column in df.columns:

    z = ((df[column] - df[column].mean()) / df[column].std()).abs()

    count = len(df[z > 3])

    zscore_results.append((column, count))

    print(f"{column:<20} {count}")

# =============================================================================
# Save Report
# =============================================================================

with open(REPORT_FILE, "w", encoding="utf-8") as report:

    report.write("=" * 65 + "\n")
    report.write("OUTLIER ANALYSIS REPORT\n")
    report.write("=" * 65 + "\n\n")

    report.write("Dataset : order_items\n\n")

    report.write("IQR METHOD\n")
    report.write("-" * 65 + "\n")

    for col, count in iqr_results:
        report.write(f"{col:<20} {count}\n")

    report.write("\n")

    report.write("Z-SCORE METHOD\n")
    report.write("-" * 65 + "\n")

    for col, count in zscore_results:
        report.write(f"{col:<20} {count}\n")

    report.write("\n")
    report.write("Observation\n")
    report.write("-" * 65 + "\n")
    report.write("• IQR detected more outliers.\n")
    report.write("• Z-Score detected fewer outliers.\n")
    report.write("• IQR is more suitable for skewed distributions.\n")
    report.write("• Z-Score works better for approximately normal distributions.\n")

print("\n")
print("=" * 60)
print("REPORT GENERATED SUCCESSFULLY")
print("=" * 60)
print(REPORT_FILE)