"""
Project : Data Foundations: SQL Extraction, Cleaning & Outlier Audit
Course  : Data Analytics with Gen & Agentic AI
Capstone: Part 1

File    : data_cleaning.py
Task    : Task 7 - Data Cleaning

Objective:
Load the CSV exported from Task 6, audit missing values, apply an explicit
imputation strategy, detect and remove duplicate rows, and save the cleaned
dataset.

Author  : Bhuvaneswari Yennapusala
"""

import os
import pandas as pd


# ============================================================================
# PROJECT DIRECTORIES
# ============================================================================

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

INPUT_FILE = os.path.join(
    BASE_DIR,
    "output",
    "reports",
    "orders_customers_join.csv"
)

CLEANED_FOLDER = os.path.join(
    BASE_DIR,
    "data",
    "cleaned"
)

REPORT_FOLDER = os.path.join(
    BASE_DIR,
    "output",
    "reports"
)

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


# ============================================================================
# LOAD DATASET
# ============================================================================

print("=" * 70)
print("TASK 7 - DATA CLEANING")
print("=" * 70)

print("\nLoading dataset...")

df = pd.read_csv(INPUT_FILE)

rows_before_cleaning = len(df)
columns_count = len(df.columns)

print(f"Rows    : {rows_before_cleaning}")
print(f"Columns : {columns_count}")


# ============================================================================
# MISSING VALUE AUDIT - BEFORE CLEANING
# ============================================================================

print("\n" + "=" * 70)
print("MISSING VALUE AUDIT - BEFORE CLEANING")
print("=" * 70)

missing_before = df.isnull().sum()

missing_percentage_before = (
    missing_before / len(df) * 100
).round(2)

missing_report = pd.DataFrame({
    "Missing Values": missing_before,
    "Percentage (%)": missing_percentage_before
})

print(missing_report)


# ============================================================================
# MISSING VALUE TREATMENT
# ============================================================================

print("\n" + "=" * 70)
print("APPLYING MISSING VALUE TREATMENT")
print("=" * 70)

treatment_details = []

for column in df.columns:

    missing_count = df[column].isnull().sum()

    # No missing values
    if missing_count == 0:

        treatment_details.append(
            f"{column}: No missing values. No imputation required."
        )

        continue

    # Categorical / text columns
    if df[column].dtype == "object":

        mode = df[column].mode()

        if not mode.empty:

            fill_value = mode.iloc[0]

            df[column] = df[column].fillna(fill_value)

            treatment_details.append(
                f"{column}: Categorical column. "
                f"Missing values filled using mode = '{fill_value}'."
            )

        else:

            df[column] = df[column].fillna("unknown")

            treatment_details.append(
                f"{column}: Categorical column with no available mode. "
                f"Missing values filled with 'unknown'."
            )

    # Numeric columns
    else:

        median_value = df[column].median()

        df[column] = df[column].fillna(median_value)

        treatment_details.append(
            f"{column}: Numeric column. "
            f"Missing values filled using median = {median_value}."
        )


# ============================================================================
# MISSING VALUE AUDIT - AFTER CLEANING
# ============================================================================

print("\n" + "=" * 70)
print("MISSING VALUE AUDIT - AFTER CLEANING")
print("=" * 70)

missing_after = df.isnull().sum()

missing_percentage_after = (
    missing_after / len(df) * 100
).round(2)

missing_after_report = pd.DataFrame({
    "Missing Values": missing_after,
    "Percentage (%)": missing_percentage_after
})

print(missing_after_report)

total_missing_after = int(missing_after.sum())

print(f"\nTotal missing values after cleaning: {total_missing_after}")

if total_missing_after == 0:
    print("PASS: No missing values remain after cleaning.")
else:
    print("WARNING: Missing values still remain.")


# ============================================================================
# DUPLICATE ROW AUDIT
# ============================================================================

print("\n" + "=" * 70)
print("DUPLICATE ROW AUDIT")
print("=" * 70)

duplicate_count_before = int(df.duplicated().sum())

print(f"Duplicate rows before removal: {duplicate_count_before}")

df = df.drop_duplicates()

rows_after_cleaning = len(df)

duplicate_count_after = int(df.duplicated().sum())

duplicate_rows_removed = (
    rows_before_cleaning - rows_after_cleaning
)

print(f"Rows before cleaning          : {rows_before_cleaning}")
print(f"Rows after cleaning           : {rows_after_cleaning}")
print(f"Duplicate rows removed        : {duplicate_rows_removed}")
print(f"Duplicate rows after removal  : {duplicate_count_after}")


# ============================================================================
# FINAL DATASET VALIDATION
# ============================================================================

print("\n" + "=" * 70)
print("FINAL DATASET VALIDATION")
print("=" * 70)

final_missing_count = int(df.isnull().sum().sum())
final_duplicate_count = int(df.duplicated().sum())

print(f"Final rows              : {len(df)}")
print(f"Final columns           : {len(df.columns)}")
print(f"Final missing values    : {final_missing_count}")
print(f"Final duplicate rows    : {final_duplicate_count}")


# ============================================================================
# SAVE CLEANED DATASET
# ============================================================================

df.to_csv(
    OUTPUT_FILE,
    index=False
)

print("\n" + "=" * 70)
print("CLEANED DATASET SAVED SUCCESSFULLY")
print("=" * 70)

print(f"Output file: {OUTPUT_FILE}")


# ============================================================================
# GENERATE DATA CLEANING REPORT
# ============================================================================

with open(
    REPORT_FILE,
    "w",
    encoding="utf-8"
) as report:

    report.write("=" * 70 + "\n")
    report.write("DATA CLEANING REPORT\n")
    report.write("=" * 70 + "\n\n")

    report.write("PROJECT INFORMATION\n")
    report.write("-" * 70 + "\n")
    report.write(
        "Project: Data Foundations: SQL Extraction, Cleaning & Outlier Audit\n"
    )
    report.write(
        "Task: Task 7 - Data Cleaning\n"
    )
    report.write(
        "Dataset: Olist Brazilian E-Commerce Dataset\n\n"
    )

    # ------------------------------------------------------------------------
    # FILE INFORMATION
    # ------------------------------------------------------------------------

    report.write("FILE INFORMATION\n")
    report.write("-" * 70 + "\n")
    report.write(f"Input File : {INPUT_FILE}\n")
    report.write(f"Output File: {OUTPUT_FILE}\n\n")

    # ------------------------------------------------------------------------
    # DATASET SIZE
    # ------------------------------------------------------------------------

    report.write("DATASET SIZE\n")
    report.write("-" * 70 + "\n")
    report.write(
        f"Rows Before Cleaning : {rows_before_cleaning}\n"
    )
    report.write(
        f"Rows After Cleaning  : {rows_after_cleaning}\n"
    )
    report.write(
        f"Columns              : {columns_count}\n"
    )
    report.write(
        f"Duplicate Rows Removed: {duplicate_rows_removed}\n\n"
    )

    # ------------------------------------------------------------------------
    # MISSING VALUES BEFORE CLEANING
    # ------------------------------------------------------------------------

    report.write("MISSING VALUES - BEFORE CLEANING\n")
    report.write("-" * 70 + "\n")
    report.write(
        missing_report.to_string()
    )
    report.write("\n\n")

    # ------------------------------------------------------------------------
    # MISSING VALUES AFTER CLEANING
    # ------------------------------------------------------------------------

    report.write("MISSING VALUES - AFTER CLEANING\n")
    report.write("-" * 70 + "\n")
    report.write(
        missing_after_report.to_string()
    )
    report.write("\n\n")

    report.write(
        f"Total Missing Values After Cleaning: "
        f"{total_missing_after}\n\n"
    )

    # ------------------------------------------------------------------------
    # DUPLICATE AUDIT
    # ------------------------------------------------------------------------

    report.write("DUPLICATE ROW AUDIT\n")
    report.write("-" * 70 + "\n")

    report.write(
        f"Duplicate Rows Before Removal: "
        f"{duplicate_count_before}\n"
    )

    report.write(
        f"Duplicate Rows After Removal : "
        f"{duplicate_count_after}\n"
    )

    report.write(
        f"Duplicate Rows Removed       : "
        f"{duplicate_rows_removed}\n\n"
    )

    # ------------------------------------------------------------------------
    # TREATMENT DETAILS
    # ------------------------------------------------------------------------

    report.write("MISSING VALUE TREATMENT\n")
    report.write("-" * 70 + "\n")

    for treatment in treatment_details:
        report.write(f"- {treatment}\n")

    report.write("\n")

    # ------------------------------------------------------------------------
    # JUSTIFICATION
    # ------------------------------------------------------------------------

    report.write("IMPUTATION STRATEGY JUSTIFICATION\n")
    report.write("-" * 70 + "\n")

    report.write(
        "Numeric columns use median imputation because the median is "
        "less sensitive to extreme values and is therefore more robust "
        "when numerical data may contain outliers.\n\n"
    )

    report.write(
        "Categorical columns use mode imputation because the mode "
        "represents the most frequently occurring category and preserves "
        "the existing categorical distribution. If no valid mode exists, "
        "the value 'unknown' is used.\n\n"
    )

    report.write(
        "Duplicate rows are identified and removed using Pandas "
        "drop_duplicates() so that repeated records do not affect "
        "subsequent statistical analysis and outlier detection.\n\n"
    )

    # ------------------------------------------------------------------------
    # FINAL VALIDATION
    # ------------------------------------------------------------------------

    report.write("FINAL VALIDATION\n")
    report.write("-" * 70 + "\n")

    report.write(
        f"Final Missing Values : {final_missing_count}\n"
    )

    report.write(
        f"Final Duplicate Rows : {final_duplicate_count}\n"
    )

    if final_missing_count == 0:
        report.write(
            "Missing-value validation: PASS\n"
        )
    else:
        report.write(
            "Missing-value validation: REVIEW REQUIRED\n"
        )

    if final_duplicate_count == 0:
        report.write(
            "Duplicate validation: PASS\n"
        )
    else:
        report.write(
            "Duplicate validation: REVIEW REQUIRED\n"
        )

    report.write("\n")
    report.write("=" * 70 + "\n")
    report.write("END OF DATA CLEANING REPORT\n")
    report.write("=" * 70 + "\n")


# ============================================================================
# COMPLETION MESSAGE
# ============================================================================

print("\n" + "=" * 70)
print("TASK 7 COMPLETED")
print("=" * 70)

print(f"Cleaned Dataset : {OUTPUT_FILE}")
print(f"Cleaning Report : {REPORT_FILE}")

print("=" * 70)