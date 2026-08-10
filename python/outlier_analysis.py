"""
Project : Data Foundations: SQL Extraction, Cleaning & Outlier Audit
Course  : Data Analytics with Gen & Agentic AI
Capstone: Part 1

File    : outlier_analysis.py
Task    : Task 8 - Outlier Audit

Objective:
Identify continuous numeric business measures and detect outliers using
both IQR and Z-score methods.

Filtering rule:
Only continuous numeric measures are considered.
Identifier/key columns, categorical columns, binary/flag columns,
and zero/near-zero variance columns are excluded.

Author : Bhuvaneswari Yennapusala
"""

import os
import pandas as pd
from sqlalchemy import create_engine


# ============================================================================
# DATABASE CONFIGURATION
# ============================================================================

HOST = "localhost"
PORT = 3306
USER = "root"
PASSWORD = ""
DATABASE = "smartcommerce_analytics"


# ============================================================================
# PROJECT DIRECTORIES
# ============================================================================

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

REPORT_FOLDER = os.path.join(
    BASE_DIR,
    "output",
    "reports"
)

os.makedirs(
    REPORT_FOLDER,
    exist_ok=True
)

REPORT_FILE = os.path.join(
    REPORT_FOLDER,
    "outlier_analysis_report.txt"
)


# ============================================================================
# DATABASE CONNECTION
# ============================================================================

engine = None

try:

    print("=" * 70)
    print("TASK 8 - OUTLIER AUDIT")
    print("=" * 70)

    print("\nConnecting to MySQL/MariaDB...")

    engine = create_engine(
        f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
    )


    # ========================================================================
    # LOAD CONTINUOUS NUMERIC BUSINESS MEASURES
    # ========================================================================
    #
    # price and freight_value are continuous numeric business measures.
    #
    # We intentionally do NOT include:
    # - order_id
    # - product_id
    # - order_item_id
    # - other identifiers
    #
    # because identifiers are not meaningful continuous measurements.
    # ========================================================================

    query = """
    SELECT
        price,
        freight_value
    FROM order_items;
    """

    print("\nLoading continuous numeric measures...")

    df = pd.read_sql(
        query,
        engine
    )

    print(f"Rows loaded: {len(df)}")
    print(f"Columns loaded: {list(df.columns)}")


    # ========================================================================
    # APPLY FILTERING RULE
    # ========================================================================

    print("\n" + "=" * 70)
    print("CONTINUOUS NUMERIC MEASURE FILTER")
    print("=" * 70)

    numeric_columns = df.select_dtypes(
        include="number"
    ).columns.tolist()

    selected_columns = []

    excluded_columns = {}

    for column in numeric_columns:

        unique_count = df[column].nunique(dropna=True)

        variance = df[column].var()

        column_lower = column.lower()

        # ---------------------------------------------------------------
        # Exclude identifier/key columns
        # ---------------------------------------------------------------

        if (
            column_lower.endswith("_id")
            or column_lower == "id"
            or "id" in column_lower
        ):

            excluded_columns[column] = "Identifier/key column"
            continue

        # ---------------------------------------------------------------
        # Exclude binary/flag columns
        # ---------------------------------------------------------------

        if unique_count <= 2:

            excluded_columns[column] = (
                "Binary/flag-like column"
            )
            continue

        # ---------------------------------------------------------------
        # Exclude zero/near-zero variance columns
        # ---------------------------------------------------------------

        if pd.isna(variance) or variance <= 1e-12:

            excluded_columns[column] = (
                "Zero/near-zero variance column"
            )
            continue

        # ---------------------------------------------------------------
        # Otherwise keep as continuous numeric measure
        # ---------------------------------------------------------------

        selected_columns.append(column)


    print("\nSelected continuous numeric measures:")

    for column in selected_columns:
        print(f"  ✓ {column}")


    if excluded_columns:

        print("\nExcluded columns:")

        for column, reason in excluded_columns.items():
            print(f"  - {column}: {reason}")


    # ========================================================================
    # SAFETY CHECK
    # ========================================================================

    if not selected_columns:

        raise ValueError(
            "No continuous numeric measures remained after filtering."
        )


    # ========================================================================
    # IQR ANALYSIS
    # ========================================================================

    print("\n" + "=" * 70)
    print("IQR METHOD")
    print("=" * 70)

    iqr_results = []

    for column in selected_columns:

        series = df[column].dropna()

        Q1 = series.quantile(0.25)
        Q3 = series.quantile(0.75)

        IQR = Q3 - Q1

        lower_fence = Q1 - 1.5 * IQR
        upper_fence = Q3 + 1.5 * IQR

        outlier_mask = (
            (series < lower_fence)
            |
            (series > upper_fence)
        )

        outlier_count = int(
            outlier_mask.sum()
        )

        iqr_results.append({
            "column": column,
            "Q1": Q1,
            "Q3": Q3,
            "IQR": IQR,
            "lower_fence": lower_fence,
            "upper_fence": upper_fence,
            "outlier_count": outlier_count
        })

        print(
            f"{column:<20} "
            f"Outliers: {outlier_count}"
        )


    # ========================================================================
    # Z-SCORE ANALYSIS
    # ========================================================================

    print("\n" + "=" * 70)
    print("Z-SCORE METHOD")
    print("=" * 70)

    zscore_results = []

    for column in selected_columns:

        series = df[column].dropna()

        mean = series.mean()
        std = series.std()

        z_scores = (
            (series - mean) / std
        ).abs()

        outlier_mask = z_scores > 3

        outlier_count = int(
            outlier_mask.sum()
        )

        zscore_results.append({
            "column": column,
            "mean": mean,
            "std": std,
            "threshold": 3,
            "outlier_count": outlier_count
        })

        print(
            f"{column:<20} "
            f"Outliers: {outlier_count}"
        )


    # ========================================================================
    # COMPARE IQR AND Z-SCORE RESULTS
    # ========================================================================

    comparison_results = []

    for iqr_result in iqr_results:

        column = iqr_result["column"]

        z_result = next(
            result
            for result in zscore_results
            if result["column"] == column
        )

        iqr_count = iqr_result["outlier_count"]
        z_count = z_result["outlier_count"]

        difference = iqr_count - z_count

        if iqr_count == z_count:

            comparison = "Agree"

        else:

            comparison = "Disagree"

        comparison_results.append({
            "column": column,
            "iqr_count": iqr_count,
            "zscore_count": z_count,
            "difference": difference,
            "comparison": comparison
        })


    # ========================================================================
    # GENERATE REPORT
    # ========================================================================

    with open(
        REPORT_FILE,
        "w",
        encoding="utf-8"
    ) as report:

        report.write("=" * 70 + "\n")
        report.write("OUTLIER ANALYSIS REPORT\n")
        report.write("=" * 70 + "\n\n")

        report.write(
            "Project: Data Foundations: SQL Extraction, "
            "Cleaning & Outlier Audit\n"
        )

        report.write(
            "Task: Task 8 - Outlier Audit\n"
        )

        report.write(
            "Dataset/Table: order_items\n\n"
        )


        # --------------------------------------------------------------------
        # FILTERING RULE
        # --------------------------------------------------------------------

        report.write(
            "CONTINUOUS NUMERIC MEASURE FILTERING RULE\n"
        )

        report.write("-" * 70 + "\n")

        report.write(
            "Only continuous numeric business measures are included "
            "in the outlier audit.\n"
        )

        report.write(
            "Identifier/key columns are excluded because their numeric "
            "values represent labels rather than measurements.\n"
        )

        report.write(
            "Binary/flag columns and zero/near-zero variance columns "
            "are also excluded because they are not meaningful "
            "continuous measures.\n\n"
        )


        # --------------------------------------------------------------------
        # SELECTED COLUMNS
        # --------------------------------------------------------------------

        report.write(
            "SELECTED CONTINUOUS NUMERIC MEASURES\n"
        )

        report.write("-" * 70 + "\n")

        for column in selected_columns:
            report.write(
                f"- {column}\n"
            )

        report.write("\n")


        # --------------------------------------------------------------------
        # EXCLUDED COLUMNS
        # --------------------------------------------------------------------

        report.write(
            "EXCLUDED COLUMNS\n"
        )

        report.write("-" * 70 + "\n")

        if excluded_columns:

            for column, reason in excluded_columns.items():

                report.write(
                    f"- {column}: {reason}\n"
                )

        else:

            report.write(
                "No columns were excluded.\n"
            )

        report.write("\n")


        # --------------------------------------------------------------------
        # IQR RESULTS
        # --------------------------------------------------------------------

        report.write(
            "IQR METHOD\n"
        )

        report.write("-" * 70 + "\n")

        report.write(
            "Rule: Outliers are values below Q1 - 1.5*IQR "
            "or above Q3 + 1.5*IQR.\n\n"
        )

        for result in iqr_results:

            report.write(
                f"Column: {result['column']}\n"
            )

            report.write(
                f"Q1          : {result['Q1']:.6f}\n"
            )

            report.write(
                f"Q3          : {result['Q3']:.6f}\n"
            )

            report.write(
                f"IQR         : {result['IQR']:.6f}\n"
            )

            report.write(
                f"Lower Fence : {result['lower_fence']:.6f}\n"
            )

            report.write(
                f"Upper Fence : {result['upper_fence']:.6f}\n"
            )

            report.write(
                f"Outliers    : {result['outlier_count']}\n\n"
            )


        # --------------------------------------------------------------------
        # Z-SCORE RESULTS
        # --------------------------------------------------------------------

        report.write(
            "Z-SCORE METHOD\n"
        )

        report.write("-" * 70 + "\n")

        report.write(
            "Rule: Values with absolute Z-score greater than 3 "
            "are classified as outliers.\n\n"
        )

        for result in zscore_results:

            report.write(
                f"Column: {result['column']}\n"
            )

            report.write(
                f"Mean        : {result['mean']:.6f}\n"
            )

            report.write(
                f"Std Dev     : {result['std']:.6f}\n"
            )

            report.write(
                f"Z Threshold : {result['threshold']}\n"
            )

            report.write(
                f"Outliers    : {result['outlier_count']}\n\n"
            )


        # --------------------------------------------------------------------
        # COMPARISON
        # --------------------------------------------------------------------

        report.write(
            "IQR VS Z-SCORE COMPARISON\n"
        )

        report.write("-" * 70 + "\n")

        for result in comparison_results:

            report.write(
                f"Column: {result['column']}\n"
            )

            report.write(
                f"IQR Outliers     : {result['iqr_count']}\n"
            )

            report.write(
                f"Z-score Outliers : {result['zscore_count']}\n"
            )

            report.write(
                f"Difference       : {result['difference']}\n"
            )

            report.write(
                f"Result           : {result['comparison']}\n\n"
            )


        # --------------------------------------------------------------------
        # ONE-LINE EXPLANATION
        # --------------------------------------------------------------------

        report.write(
            "METHOD DIFFERENCE EXPLANATION\n"
        )

        report.write("-" * 70 + "\n")

        report.write(
            "IQR is distribution-free and is generally more robust to "
            "skewed data and extreme values, whereas Z-score relies on "
            "the mean and standard deviation and is most appropriate "
            "when the distribution is approximately normal. Therefore, "
            "the two methods can identify different observations when "
            "the data are skewed or contain extreme values.\n\n"
        )


        # --------------------------------------------------------------------
        # FINAL SUMMARY
        # --------------------------------------------------------------------

        report.write(
            "FINAL SUMMARY\n"
        )

        report.write("-" * 70 + "\n")

        for result in comparison_results:

            report.write(
                f"{result['column']}: "
                f"IQR={result['iqr_count']}, "
                f"Z-score={result['zscore_count']}, "
                f"{result['comparison']}\n"
            )


        report.write("\n")
        report.write("=" * 70 + "\n")
        report.write("END OF OUTLIER ANALYSIS REPORT\n")
        report.write("=" * 70 + "\n")


    # ========================================================================
    # COMPLETION MESSAGE
    # ========================================================================

    print("\n" + "=" * 70)
    print("TASK 8 REPORT GENERATED SUCCESSFULLY")
    print("=" * 70)

    print(f"Report: {REPORT_FILE}")

    print("=" * 70)


except Exception as error:

    print("\n" + "=" * 70)
    print("TASK 8 FAILED")
    print("=" * 70)

    print(error)

    print("=" * 70)


finally:

    if engine is not None:

        engine.dispose()

        print("\nDatabase connection closed.")