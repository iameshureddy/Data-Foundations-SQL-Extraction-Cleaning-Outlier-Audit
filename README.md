# Data Foundations: SQL Extraction, Cleaning & Outlier Audit

**Capstone Project – Part 1**

**Student Name:** Bhuvaneswari Yennapusala

**Program:** Data Analytics with Gen & Agentic AI

**Organization:** Masai School

---

# Project Overview

This project demonstrates the end-to-end process of extracting, validating, cleaning, and analyzing data using SQL and Python.

A relational database is created using the Olist Brazilian E-Commerce dataset. SQL is used to perform data extraction, filtering, aggregation, JOIN operations, and referential integrity validation. The extracted data is exported to CSV and further processed using Python for data cleaning and statistical outlier detection.

The project has been developed according to the requirements specified in the **Data Foundations: SQL Extraction, Cleaning & Outlier Audit (Part 1)** assessment.

---

# Dataset

**Dataset Used:** Olist Brazilian E-Commerce Public Dataset

The Olist dataset is a publicly available relational e-commerce dataset containing information about customers, orders, products, payments, and customer reviews. It is widely used for learning SQL, data analysis, and database management concepts.

## Tables Used

| Table Name | Description |
|------------|-------------|
| customers | Customer information |
| orders | Order details |
| products | Product information |
| order_items | Products included in each order |
| payments | Payment details |
| reviews | Customer review information |

---

# Technology Stack

| Technology | Purpose |
|------------|---------|
| MySQL / MariaDB | Database Management |
| SQL | Data Extraction & Querying |
| Python | Data Cleaning & Outlier Analysis |
| Pandas | Data Manipulation |
| NumPy | Numerical Computation |
| Matplotlib | Data Visualization |
| Git & GitHub | Version Control |
| Visual Studio Code | Development Environment |

---

# Project Structure

```text
Data-Foundations-SQL-Extraction-Cleaning-Outlier-Audit/

├── database/
│   ├── 01_schema.sql
│   └── 02_import_data.sql
│
├── sql/
│   ├── 03_basic_queries.sql
│   ├── 04_groupby_having.sql
│   ├── 05_joins.sql
│   └── 06_integrity_checks.sql
│
├── python/
│   ├── config.py
│   ├── export_csv.py
│   ├── data_cleaning.py
│   ├── outlier_analysis.py
│   └── generate_visualizations.py
│
├── data/
│   ├── raw/
│   └── cleaned/
│
├── output/
│   │
│   ├── reports/
│   └── visualizations/
│
├── images/
│
├── requirements.txt
├── LICENSE
├── README.md
└── .gitignore
```

---

# Project Workflow

```text
Import Dataset
      │
      ▼
Create Relational Database
      │
      ▼
Execute SQL Queries
      │
      ▼
Perform JOIN Operations
      │
      ▼
Validate Referential Integrity
      │
      ▼
Export JOIN Results to CSV
      │
      ▼
Clean Data Using Python
      │
      ▼
Detect Outliers
      │
      ▼
Generate Reports and Visualizations
```

---

# Database Schema

The project uses a relational database named **smartcommerce_analytics** to store and manage the Olist Brazilian E-Commerce dataset.

## Tables

| Table | Description |
|--------|-------------|
| customers | Stores customer information |
| orders | Stores order details |
| products | Stores product information |
| order_items | Stores products associated with each order |
| payments | Stores payment information |
| reviews | Stores customer reviews |

---

## Primary Keys

| Table | Primary Key |
|--------|-------------|
| customers | customer_id |
| orders | order_id |
| products | product_id |
| order_items | (order_id, order_item_id) |
| payments | (order_id, payment_sequential) |
| reviews | review_id |

---

## Foreign Keys

| Child Table | Foreign Key | References |
|-------------|-------------|------------|
| orders | customer_id | customers(customer_id) |
| order_items | order_id | orders(order_id) |
| order_items | product_id | products(product_id) |
| payments | order_id | orders(order_id) |
| reviews | order_id | orders(order_id) |

---

## Entity Relationships

- One customer can place multiple orders.
- One order can contain multiple order items.
- One product can appear in multiple orders.
- One order can have one or more payment records.
- One order can have one customer review.

---

# Task 1 – Relational Database Setup

## Objective

Create a relational database with Primary Key and Foreign Key relationships.

## Implementation

- Created the `smartcommerce_analytics` database.
- Imported the Olist Brazilian E-Commerce dataset into MySQL/MariaDB.
- Defined Primary Key constraints for all tables.
- Established Foreign Key relationships between related tables.

## Files Used

```text
database/
├── 01_schema.sql
└── 02_import_data.sql
```

## Result

Relational database created successfully with valid Primary Key and Foreign Key relationships.

---

# Task 2 – SQL Data Extraction

## Objective

Extract data using the required SQL query techniques.

## SQL Queries Implemented

- WHERE ... IN
- WHERE ... NOT IN
- BETWEEN
- ORDER BY (Ascending & Descending)
- LIKE
- NOT EXISTS

## File Used

```text
sql/03_basic_queries.sql
```

## Result

Successfully implemented all six required SQL query types.

---

# Task 3 – GROUP BY & HAVING

## Objective

Perform grouped analysis using aggregate functions.

## SQL Clauses Used

- GROUP BY
- HAVING

## Aggregate Functions Used

- COUNT()
- AVG()
- SUM()

## File Used

```text
sql/04_groupby_having.sql
```

## Result

Successfully performed grouped analysis using aggregate functions and HAVING.

---

# Task 4 – JOIN Operations

## Objective

Retrieve related data using INNER JOIN and LEFT JOIN.

## JOIN Types

- INNER JOIN
- LEFT JOIN

## File Used

```text
sql/05_joins.sql
```

## JOIN Justification

**INNER JOIN**

Returns only records with matching values in both tables.

**LEFT JOIN**

The `orders` table is placed on the left side to retain every order, including records without matching values in the joined table. This ensures complete order information is preserved before exporting the dataset.

## Result

Successfully implemented both JOIN operations.

---

# Task 5 – Referential Integrity Validation

## Objective

Validate table relationships before analysis.

## Validation Performed

- COUNT(DISTINCT)
- Grouped Child Count
- Orphan Record Check

## File Used

```text
sql/06_integrity_checks.sql
```

## Referential Integrity Result

**Relationship Verified**

- Parent Table: `orders`
- Child Table: `order_items`
- Relationship Type: One-to-Many (1:N)

**Validation Summary**

- COUNT(DISTINCT) validation completed successfully.
- Parent-child relationship verified using grouped child-count analysis.
- Orphan record check completed successfully.
- No orphan records were found.

---

# Task 6 – Export JOIN Result to CSV

## Objective

Export the JOIN result for Python processing.

## File Used

```text
python/export_csv.py
```

## Output

```text
output/reports/orders_customers_join.csv
```

## Export Summary

| Metric | Value |
|---------|------:|
| Rows Exported | 99,441 |
| Columns Exported | 6 |

## Result

Successfully exported the JOIN result to CSV for further processing.

---

# Task 7 – Data Cleaning

## Objective

Clean the exported CSV using Python (Pandas).

## Operations Performed

- Missing Value Count
- Missing Value Percentage
- Duplicate Detection
- Duplicate Removal
- Missing Value Imputation

## File Used

```text
python/data_cleaning.py
```

## Missing Value Summary

| Column | Missing Values | Percentage |
|---------|---------------:|-----------:|
| customer_id | 0 | 0.0% |
| customer_city | 0 | 0.0% |
| customer_state | 0 | 0.0% |
| order_id | 0 | 0.0% |
| order_status | 0 | 0.0% |
| order_purchase_timestamp | 0 | 0.0% |

## Imputation Strategy

- Numeric Columns → Median
- Categorical Columns → Mode

Median was selected because it is more robust to outliers than the mean. Mode would be used for categorical columns if missing values were present.

Since the exported dataset contained no missing values, no imputation was required.

## Duplicate Summary

| Metric | Value |
|---------|------:|
| Rows Before Cleaning | 99,441 |
| Rows After Cleaning | 99,441 |
| Duplicate Rows Removed | 0 |

## Outputs

```text
data/cleaned/cleaned_orders.csv

output/reports/data_cleaning_report.txt
```

## Result

Successfully cleaned the exported dataset and generated the cleaning report.

---

# Task 8 – Outlier Analysis

## Objective

Identify outliers using both statistical methods.

## Continuous Numeric Filtering Rule

A continuous numeric measure is any numeric column representing measurable values.

The following columns were excluded:

- Primary Key columns
- Foreign Key columns
- Date columns
- Text columns
- Binary columns
- Columns with zero or near-zero variance

Continuous numeric columns analysed:

- price
- freight_value

## Methods Used

- Interquartile Range (IQR)
- Z-score

## File Used

```text
python/outlier_analysis.py
```

## Analysis Note

Outlier analysis was performed directly on the MySQL database because the continuous numeric columns (`price` and `freight_value`) required for statistical analysis are not present in the exported CSV used for Task 7.

Rows Analysed: **112,650**

## Outlier Summary

| Column | IQR Method | Z-score Method |
|---------|-----------:|---------------:|
| price | 8,427 | 1,966 |
| freight_value | 12,134 | 2,041 |

## Method Comparison

The IQR method detected more outliers because it is more robust for skewed distributions. The Z-score method detected fewer outliers because it assumes an approximately normal distribution.

## Output

```text
output/reports/outlier_analysis_report.txt
```

## Result

Successfully completed outlier analysis using both IQR and Z-score methods.

---

# Additional Visualizations

The project also generates exploratory visualizations using Matplotlib.

| Visualization | Description |
|---------------|-------------|
| monthly_orders.png | Monthly order trend |
| orders_by_year.png | Year-wise order distribution |
| orders_by_state.png | Orders by state |
| top10_cities.png | Top 10 cities by order count |
| order_status_distribution.png | Order status distribution |
| top_states_pie.png | State-wise order share |

## Location

```text
images/plots/
```

---

# Project Outputs

```text
output/reports/
├── orders_customers_join.csv
├── data_cleaning_report.txt
├── outlier_analysis_report.txt
└── visualization_report.txt

data/cleaned/
└── cleaned_orders.csv

images/plots/
├── monthly_orders.png
├── orders_by_year.png
├── orders_by_state.png
├── top10_cities.png
├── order_status_distribution.png
└── top_states_pie.png
```


# How to Run

## 1. Clone the Repository

```bash
git clone https://github.com/iameshureddy/Data-Foundations-SQL-Extraction-Cleaning-Outlier-Audit.git
cd Data-Foundations-SQL-Extraction-Cleaning-Outlier-Audit
```

## 2. Configure Database

- Install MySQL or MariaDB.
- Create the `smartcommerce_analytics` database.
- Update the database credentials in `python/config.py`.

## 3. Create Database and Import Data

Run:

```text
database/
├── 01_schema.sql
└── 02_import_data.sql
```

## 4. Execute SQL Tasks

Run the SQL files in order:

```text
sql/
├── 03_basic_queries.sql
├── 04_groupby_having.sql
├── 05_joins.sql
└── 06_integrity_checks.sql
```

## 5. Export the JOIN Result

```bash
python python/export_csv.py
```

## 6. Clean the Exported CSV

```bash
python python/data_cleaning.py
```

## 7. Perform Outlier Analysis

```bash
python python/outlier_analysis.py
```

## 8. Generate Visualizations

```bash
python python/generate_visualizations.py
```

# Conclusion

This project successfully demonstrates the complete workflow of SQL-based data extraction, referential integrity validation, CSV export, data cleaning, and statistical outlier analysis using the Olist Brazilian E-Commerce dataset.

All required SQL queries, JOIN operations, integrity checks, Python data cleaning tasks, and outlier detection methods were implemented successfully. The generated reports and visualizations provide additional insights into the dataset and support further analysis.
