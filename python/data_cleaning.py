"""
===============================================================================
Project : Data Foundations: SQL Extraction, Cleaning & Outlier Audit
Course  : Data Analytics with Gen & Agentic AI
Capstone: Part 1

File    : data_cleaning.py

Author  : Bhuvaneswari Yennapusala

Description:
Loads the exported dataset, performs missing value handling,
duplicate removal, saves the cleaned dataset, and generates
a data cleaning report.
===============================================================================
"""

import os
import pandas as pd

# =============================================================================
# Project Directories
# =============================================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

INPUT_FILE = os.path.join(
    BASE_DIR,
    "output",
    "reports",
    "orders_customers_join.csv"
)

CLEANED_FOLDER = os.path.join(BASE_DIR, "data", "cleaned")
REPORT_FOLDER = os.path.join(BASE_DIR, "output", "reports")

os.makedirs(CLEANED_FOLDER, exist_ok=True)
os.makedirs(REPORT_FOLDER, exist_ok=True)

OUTPUT_FILE = os.path.join(
    CLEANED_FOLDER,
    "cleaned_orders.csv"
)

REPORT_FILE = os.path.join(
    REPORT_FOLDER,
    "data_cleaning_report.txt"
)

# =============================================================================
# Load Dataset
# =============================================================================

print("Loading dataset...")

df = pd.read_csv(INPUT_FILE)

print(f"Rows    : {len(df)}")
print(f"Columns : {len(df.columns)}")

# =============================================================================
# Missing Values
# =============================================================================

missing = df.isnull().sum()

missing_report = pd.DataFrame({
    "Missing Values": missing,
    "Percentage (%)": (missing / len(df) * 100).round(2)
})

print("\n================ Missing Values ================\n")
print(missing_report)

print("\nApplying missing value treatment...")

for column in df.columns:

    if df[column].dtype == "object":

        mode = df[column].mode()

        if not mode.empty:
            df[column] = df[column].fillna(mode.iloc[0])

    else:

        df[column] = df[column].fillna(df[column].median())

# =============================================================================
# Remove Duplicates
# =============================================================================

before = len(df)

df = df.drop_duplicates()

after = len(df)

removed = before - after

print("\nDuplicate Rows")
print(f"Before : {before}")
print(f"After  : {after}")
print(f"Removed: {removed}")

# =============================================================================
# Save Cleaned Dataset
# =============================================================================

df.to_csv(OUTPUT_FILE, index=False)

print("\n========================================")
print("Cleaned dataset saved successfully!")
print(OUTPUT_FILE)
print("========================================")

# =============================================================================
# Generate Report
# =============================================================================

with open(REPORT_FILE, "w", encoding="utf-8") as report:

    report.write("=" * 65 + "\n")
    report.write("DATA CLEANING REPORT\n")
    report.write("=" * 65 + "\n\n")

    report.write(f"Input File : {INPUT_FILE}\n")
    report.write(f"Output File: {OUTPUT_FILE}\n\n")

    report.write(f"Rows Before Cleaning : {before}\n")
    report.write(f"Rows After Cleaning  : {after}\n")
    report.write(f"Duplicate Rows Removed: {removed}\n\n")

    report.write("Missing Values\n")
    report.write("-" * 65 + "\n")

    report.write(missing_report.to_string())

    report.write("\n\nTreatment Applied\n")
    report.write("-" * 65 + "\n")
    report.write("✓ Checked missing values\n")
    report.write("✓ Filled missing values (if any)\n")
    report.write("✓ Removed duplicate rows\n")
    report.write("✓ Saved cleaned dataset\n")

print("\nData cleaning report generated successfully!")
print(REPORT_FILE)