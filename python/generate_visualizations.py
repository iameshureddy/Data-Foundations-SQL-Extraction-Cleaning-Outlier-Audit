"""
===============================================================================
Project : Data Foundations: SQL Extraction, Cleaning & Outlier Audit
Course  : Data Analytics with Gen & Agentic AI
Capstone: Part 1

File    : generate_visualizations.py

Description:
Generates exploratory visualizations from the exported SQL dataset
and saves them as PNG images inside the images/ directory.

Author  : Bhuvaneswari Yennapusala
===============================================================================
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

# =============================================================================
# Project Paths
# =============================================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_PATH = os.path.join(
    BASE_DIR,
    "output",
    "reports",
    "orders_customers_join.csv"
)

IMAGE_DIR = os.path.join(BASE_DIR, "images")
REPORT_DIR = os.path.join(BASE_DIR, "output", "reports")

os.makedirs(IMAGE_DIR, exist_ok=True)
os.makedirs(REPORT_DIR, exist_ok=True)

# =============================================================================
# Load Dataset
# =============================================================================

print("=" * 60)
print("LOADING DATASET")
print("=" * 60)

df = pd.read_csv(DATA_PATH)

print(f"Rows    : {len(df)}")
print(f"Columns : {len(df.columns)}")

print("\nColumns Found:")

for col in df.columns:
    print(f" - {col}")

# =============================================================================
# Date Handling
# =============================================================================

if "order_purchase_timestamp" in df.columns:

    df["order_purchase_timestamp"] = (
        df["order_purchase_timestamp"]
        .replace("0000-00-00 00:00:00", pd.NA)
    )

    df["order_purchase_timestamp"] = pd.to_datetime(
        df["order_purchase_timestamp"],
        errors="coerce"
    )

    df = df.dropna(subset=["order_purchase_timestamp"])

# =============================================================================
# Chart 1 : Orders by State
# =============================================================================

if "customer_state" in df.columns:

    plt.figure(figsize=(10,6))

    (
        df["customer_state"]
        .value_counts()
        .sort_values(ascending=False)
        .plot(kind="bar")
    )

    plt.title("Orders by State")
    plt.xlabel("State")
    plt.ylabel("Number of Orders")
    plt.tight_layout()

    plt.savefig(os.path.join(IMAGE_DIR, "orders_by_state.png"))

    plt.close()

# =============================================================================
# Chart 2 : Top 10 Cities
# =============================================================================

if "customer_city" in df.columns:

    plt.figure(figsize=(12,6))

    (
        df["customer_city"]
        .value_counts()
        .head(10)
        .plot(kind="bar")
    )

    plt.title("Top 10 Cities by Orders")
    plt.xlabel("City")
    plt.ylabel("Orders")
    plt.tight_layout()

    plt.savefig(os.path.join(IMAGE_DIR, "top10_cities.png"))

    plt.close()

# =============================================================================
# Chart 3 : Order Status
# =============================================================================

if "order_status" in df.columns:

    plt.figure(figsize=(8,5))

    (
        df["order_status"]
        .value_counts()
        .plot(kind="bar")
    )

    plt.title("Order Status Distribution")
    plt.xlabel("Order Status")
    plt.ylabel("Count")
    plt.tight_layout()

    plt.savefig(os.path.join(IMAGE_DIR, "order_status_distribution.png"))

    plt.close()

# =============================================================================
# Chart 4 : Monthly Orders
# =============================================================================

if "order_purchase_timestamp" in df.columns:

    monthly_orders = (
        df.groupby(
            df["order_purchase_timestamp"].dt.to_period("M")
        )
        .size()
    )

    monthly_orders.index = monthly_orders.index.astype(str)

    plt.figure(figsize=(12,6))

    monthly_orders.plot(marker="o")

    plt.title("Monthly Orders")
    plt.xlabel("Month")
    plt.ylabel("Orders")
    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.savefig(os.path.join(IMAGE_DIR, "monthly_orders.png"))

    plt.close()

# =============================================================================
# Chart 5 : Orders by Year
# =============================================================================

if "order_purchase_timestamp" in df.columns:

    yearly_orders = (
        df.groupby(
            df["order_purchase_timestamp"].dt.year
        )
        .size()
    )

    plt.figure(figsize=(8,5))

    yearly_orders.plot(kind="bar")

    plt.title("Orders by Year")
    plt.xlabel("Year")
    plt.ylabel("Orders")

    plt.tight_layout()

    plt.savefig(os.path.join(IMAGE_DIR, "orders_by_year.png"))

    plt.close()

# =============================================================================
# Chart 6 : Top States Pie Chart
# =============================================================================

if "customer_state" in df.columns:

    plt.figure(figsize=(8,8))

    (
        df["customer_state"]
        .value_counts()
        .head(10)
        .plot(kind="pie", autopct="%1.1f%%")
    )

    plt.ylabel("")

    plt.title("Top 10 States")

    plt.tight_layout()

    plt.savefig(os.path.join(IMAGE_DIR, "top_states_pie.png"))

    plt.close()

# =============================================================================
# Report
# =============================================================================

report_path = os.path.join(
    REPORT_DIR,
    "visualization_report.txt"
)

with open(report_path, "w") as report:

    report.write("=" * 60 + "\n")
    report.write("VISUALIZATION REPORT\n")
    report.write("=" * 60 + "\n\n")

    report.write(f"Rows Analysed : {len(df)}\n")
    report.write(f"Columns       : {len(df.columns)}\n\n")

    report.write("Charts Generated\n")
    report.write("-----------------------------\n")
    report.write("1. Orders by State\n")
    report.write("2. Top 10 Cities\n")
    report.write("3. Order Status Distribution\n")
    report.write("4. Monthly Orders\n")
    report.write("5. Orders by Year\n")
    report.write("6. Top States Pie Chart\n")

print("\n" + "=" * 60)
print("VISUALIZATIONS GENERATED SUCCESSFULLY")
print("=" * 60)

print(f"\nImages Folder : {IMAGE_DIR}")
print(f"Report         : {report_path}")

print("\nGenerated Files")

print("------------------------------")

for file in sorted(os.listdir(IMAGE_DIR)):
    print(file)