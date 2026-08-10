# Data Foundations: SQL Extraction, Cleaning & Outlier Audit

**Course:** Data Analytics with Gen & Agentic AI
**Capstone:** Part 1
**Author:** Bhuvaneswari Yennapusala
**Database:** MySQL/MariaDB through XAMPP and phpMyAdmin
**Repository:** https://github.com/iameshureddy/Data-Foundations-SQL-Extraction-Cleaning-Outlier-Audit

---

## 1. Project Overview

This project implements **Part 1 – Data Foundations: SQL Extraction, Cleaning & Outlier Audit** of the Masai **Data Analytics with Gen & Agentic AI** capstone.

The objective is to prepare a relational business dataset for further statistical analysis and AI-based analytics by:

1. Setting up and querying a relational MySQL database.
2. Performing fundamental SQL filtering and retrieval operations.
3. Performing aggregation using `GROUP BY` and `HAVING`.
4. Joining related tables using `INNER JOIN` and `LEFT JOIN`.
5. Validating referential integrity between parent and child tables.
6. Exporting a JOIN result to CSV.
7. Cleaning the exported data using Python and Pandas.
8. Auditing continuous numeric measures for outliers using IQR and Z-score methods.
9. Documenting the results and decisions in reproducible reports.

---

# 2. Scenario

The project uses a small relational e-commerce/business database containing customer, order, product, payment, review and order-item information.

The main relationship used in Part 1 is:

```text
customers
    |
    | 1 : M
    v
orders
```

One customer can have multiple orders.

The project also uses:

```text
orders
    |
    | 1 : M
    v
order_items
```

The `order_items` table contains continuous numeric measures such as:

- `price`
- `freight_value`

These measures are used for the Task 8 outlier audit.

---

# 3. Technology Stack

| Component | Technology |
|---|---|
| Database | MySQL / MariaDB |
| Local Server | XAMPP |
| Database Interface | phpMyAdmin |
| Programming Language | Python |
| Data Processing | Pandas |
| Database Connectivity | SQLAlchemy + PyMySQL |
| Query Language | SQL |
| Export Format | CSV |
| Outlier Methods | IQR and Z-score |
| Version Control | Git and GitHub |
| Development Environment | Visual Studio Code |

---

# 4. Dataset and Database Schema

## Database

```text
smartcommerce_analytics
```

The database is created and accessed through the **XAMPP MySQL/MariaDB server** and managed using **phpMyAdmin**.

## Tables

The project database contains the following tables:

```text
smartcommerce_analytics
│
├── customers
├── orders
├── order_items
├── payments
├── products
└── reviews
```

### Main relationship

```text
customers
   │
   │ customer_id
   │
   └──────────────< orders
                    │
                    │ order_id
                    │
                    └──────────────< order_items
```

### Parent-child relationship used for Task 5

```text
customers.customer_id
        │
        │ 1 : M
        ▼
orders.customer_id
```

- `customers` acts as the parent table.
- `orders` acts as the child table.
- `customer_id` is the natural key used to relate the two tables.
- Multiple orders may belong to the same customer.

---

# 5. Project Structure

```text
Data-Foundations-SQL-Extraction-Cleaning-Outlier-Audit/
│
├── images/
│   ├── plots/
│   ├── monthly_orders.png
│   ├── order_status_distribution.png
│   ├── orders_by_state.png
│   ├── orders_by_year.png
│   ├── top10_cities.png
│   └── top_states_pie.png
│
├── output/
│   └── reports/
│       ├── orders_customers_join.csv
│       ├── data_cleaning_report.txt
│       ├── outlier_analysis_report.txt
│       └── visualization_report.txt
│
├── data/
│   └── cleaned/
│       └── cleaned_orders.csv
│
├── python/
│   ├── config.py
│   ├── export_csv.py
│   ├── data_cleaning.py
│   ├── outlier_analysis.py
│   └── generate_visualizations.py
│
├── sql/
│   ├── 03_basic_queries.sql
│   ├── 04_groupby_having.sql
│   ├── 05_joins.sql
│   └── 06_integrity_checks.sql
│
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

---

# 6. Task 1 – Relational Database Setup

A relational business database was established in MySQL/MariaDB using XAMPP.

The database:

```sql
smartcommerce_analytics
```

contains multiple related tables with primary-key/foreign-key style relationships.

The main relationship validated in this project is:

```text
customers (parent)
       |
       | customer_id
       |
       v
orders (child)
```

This relationship represents:

```text
One Customer → Many Orders
```

The database was accessed locally through:

```text
XAMPP → MySQL/MariaDB → phpMyAdmin
```

---

# 7. Task 2 – Basic SQL Queries

The SQL implementation covers the six required query techniques.

File:

```text
sql/03_basic_queries.sql
```

The query techniques include:

### 1. `IN`

Used to filter rows where a column matches one of multiple specified values.

### 2. `BETWEEN`

Used to filter values within a specified range.

### 3. `ORDER BY`

Used to sort query results in ascending or descending order.

### 4. Subquery

Used to retrieve data based on the result of another query.

### 5. `EXISTS`

Used to check whether a related record exists.

### 6. `LIKE`

Used for partial text matching with wildcard patterns such as `%`.

These queries demonstrate practical SQL filtering, searching, sorting and relational retrieval.

---

# 8. Task 3 – GROUP BY and HAVING

File:

```text
sql/04_groupby_having.sql
```

The project uses `GROUP BY` to aggregate records and `HAVING` to filter groups after aggregation.

The query uses multiple aggregate functions, including functions such as:

```sql
COUNT()
SUM()
AVG()
```

Example analytical pattern:

```sql
SELECT
    payment_type,
    COUNT(*) AS total_transactions,
    SUM(payment_value) AS total_sales,
    AVG(payment_value) AS average_payment
FROM payments
GROUP BY payment_type
HAVING SUM(payment_value) > 100000
ORDER BY total_sales DESC;
```

This produces grouped payment-level business statistics and filters groups based on an aggregate condition.

---

# 9. Task 4 – JOIN Operations

File:

```text
sql/05_joins.sql
```

Two JOIN types are implemented.

## 9.1 INNER JOIN

The `INNER JOIN` keeps only records where a matching customer exists for an order.

Example:

```sql
SELECT
    c.customer_id,
    c.customer_city,
    c.customer_state,
    o.order_id,
    o.order_status
FROM customers AS c
INNER JOIN orders AS o
    ON c.customer_id = o.customer_id;
```

### Why INNER JOIN?

The Task 6 export requires customer information associated with valid orders. Therefore, matching customer-order records are retained.

## 9.2 LEFT JOIN

The `LEFT JOIN` keeps all rows from the selected left table and identifies whether a corresponding record exists in the other table.

Example:

```sql
SELECT
    c.customer_id,
    c.customer_city,
    c.customer_state,
    o.order_id,
    o.order_status
FROM customers AS c
LEFT JOIN orders AS o
    ON c.customer_id = o.customer_id;
```

### Why LEFT JOIN?

It is useful for completeness checks because customers without matching orders can still be identified.

---

# 10. Task 5 – Referential Integrity Validation

File:

```text
sql/06_integrity_checks.sql
```

The relationship between `customers` and `orders` was validated using three checks.

## Check 1 – COUNT(DISTINCT)

The number of distinct customers having matching orders was calculated.

Result:

```text
unique_customers_with_orders = 99441
```

This confirms that **99,441 distinct customers have matching order records** in the JOIN result.

## Check 2 – One-to-Many Relationship

A grouped query was used to check whether a customer can have multiple orders:

```sql
SELECT
    o.customer_id,
    COUNT(o.order_id) AS total_orders
FROM orders AS o
GROUP BY o.customer_id
HAVING COUNT(o.order_id) > 1
ORDER BY total_orders DESC;
```

This validates the intended **1:M customer-to-order relationship**.

## Check 3 – Orphan Orders

A `LEFT JOIN` was used to find orders whose `customer_id` does not exist in `customers`.

```sql
SELECT
    o.order_id,
    o.customer_id
FROM orders AS o
LEFT JOIN customers AS c
    ON o.customer_id = c.customer_id
WHERE c.customer_id IS NULL;
```

### Result

```text
0 orphan orders
```

Therefore, no unmatched child orders were found by this validation query.

### Integrity conclusion

The executed checks support that the customer-order relationship is consistent in the loaded dataset:

```text
Customer → Orders = 1 : Many
Orphan orders     = 0
```

> Note: The project uses MySQL/MariaDB through XAMPP, so SQLite-specific `PRAGMA foreign_keys` testing is not part of this implementation.

---

# 11. Task 6 – Export JOIN Result to CSV

File:

```text
python/export_csv.py
```

The Task 4 `INNER JOIN` result was exported from MySQL into:

```text
output/reports/orders_customers_join.csv
```

The exported dataset contains the following six columns:

```text
customer_id
customer_city
customer_state
order_id
order_status
order_purchase_timestamp
```

## Export Result

```text
Rows exported    : 99441
Columns exported : 6
```

The CSV was successfully loaded using Pandas for Task 7.

---

# 12. Task 7 – Data Cleaning

File:

```text
python/data_cleaning.py
```

Input:

```text
output/reports/orders_customers_join.csv
```

Output:

```text
data/cleaned/cleaned_orders.csv
```

## 12.1 Dataset Size

```text
Rows    : 99441
Columns : 6
```

## 12.2 Missing-Value Audit

Missing values were checked for every column.

| Column | Missing Values | Percentage |
|---|---:|---:|
| customer_id | 0 | 0.00% |
| customer_city | 0 | 0.00% |
| customer_state | 0 | 0.00% |
| order_id | 0 | 0.00% |
| order_status | 0 | 0.00% |
| order_purchase_timestamp | 0 | 0.00% |

### Missing-value result

```text
Total missing values after cleaning: 0
```

Therefore:

```text
PASS: No missing values remain after cleaning.
```

## 12.3 Imputation Strategy

The cleaning script implements an explicit strategy:

- Categorical/object columns → mode
- Numeric columns → median

The strategy is applied only when missing values are present.

In the actual exported dataset, all six columns contained zero missing values, so **no imputation was required**.

### Why this strategy?

- Mode is suitable for categorical fields because it preserves a valid existing category.
- Median is more robust than mean when numeric data may contain skewness or extreme values.

## 12.4 Duplicate Audit

Duplicate rows were checked before and after removal.

```text
Rows before cleaning          : 99441
Rows after cleaning           : 99441
Duplicate rows removed        : 0
Duplicate rows after removal  : 0
```

Therefore, the exported dataset contained no duplicate rows.

## Final Cleaning Result

```text
Final rows           : 99441
Final columns        : 6
Final missing values : 0
Final duplicate rows : 0
```

---

# 13. Task 8 – Outlier Audit

File:

```text
python/outlier_analysis.py
```

The outlier analysis was performed on continuous numeric measures from:

```text
order_items
```

The selected measures were:

```text
price
freight_value
```

## Dataset Used

```text
Rows loaded    : 112650
Columns loaded: price, freight_value
```

The analysis intentionally excludes identifier/categorical fields and focuses on continuous numeric measures.

---

# 14. IQR Method

The Interquartile Range method was used.

Formula:

```text
IQR = Q3 - Q1

Lower Fence = Q1 - 1.5 × IQR

Upper Fence = Q3 + 1.5 × IQR
```

Values outside the lower and upper fences were counted as outliers.

## IQR Results

| Measure | IQR Outliers |
|---|---:|
| price | 8,427 |
| freight_value | 12,134 |

---

# 15. Z-Score Method

The Z-score was calculated for every value:

```text
Z = (x - mean) / standard deviation
```

A value was classified as an outlier when:

```text
|Z| > 3
```

## Z-Score Results

| Measure | Z-Score Outliers |
|---|---:|
| price | 1,966 |
| freight_value | 2,041 |

---

# 16. IQR vs Z-Score Comparison

| Measure | IQR | Z-Score |
|---|---:|---:|
| price | 8,427 | 1,966 |
| freight_value | 12,134 | 2,041 |

### Observation

The IQR method detected substantially more outliers than the Z-score method.

This difference can occur because the two methods use different definitions of an extreme observation:

- **IQR** uses quartiles and is robust to skewed distributions.
- **Z-score** uses mean and standard deviation and is more appropriate when the distribution is approximately normal.

For business transaction variables such as price and freight value, skewness and extreme transaction values can make the IQR method particularly useful.

The project therefore reports both methods rather than relying on only one outlier definition.

---

# 17. Task 8 Filtering Rule

The project defines a continuous numeric measure as a numeric variable representing a measurable quantity.

The analysis includes:

```text
✓ price
✓ freight_value
```

The analysis excludes:

```text
✗ IDs
✗ categorical columns
✗ binary/flag fields
✗ columns with zero or near-zero variance
```

The final selected measures were:

```text
price
freight_value
```

---

# 18. Project Results Summary

| Task | Result |
|---|---|
| Task 1 | Relational MySQL/MariaDB database established using XAMPP |
| Task 2 | Six required SQL query techniques implemented |
| Task 3 | `GROUP BY` + `HAVING` with multiple aggregates |
| Task 4 | INNER JOIN and LEFT JOIN implemented |
| Task 5 | Customer-order integrity validated; 0 orphan orders |
| Task 6 | 99,441 rows × 6 columns exported to CSV |
| Task 7 | 0 missing values and 0 duplicate rows |
| Task 8 | IQR and Z-score audit completed for price and freight_value |

---

# 19. Output Files

### SQL

```text
sql/03_basic_queries.sql
sql/04_groupby_having.sql
sql/05_joins.sql
sql/06_integrity_checks.sql
```

### Python

```text
python/export_csv.py
python/data_cleaning.py
python/outlier_analysis.py
```

### Reports

```text
output/reports/data_cleaning_report.txt
output/reports/outlier_analysis_report.txt
output/reports/orders_customers_join.csv
```

### Cleaned Dataset

```text
data/cleaned/cleaned_orders.csv
```

### Visualizations

```text
images/monthly_orders.png
images/order_status_distribution.png
images/orders_by_state.png
images/orders_by_year.png
images/top10_cities.png
images/top_states_pie.png
```

---

# 20. How to Run

## Step 1 – Clone Repository

```bash
git clone https://github.com/iameshureddy/Data-Foundations-SQL-Extraction-Cleaning-Outlier-Audit.git
cd Data-Foundations-SQL-Extraction-Cleaning-Outlier-Audit
```

## Step 2 – Start XAMPP

Open XAMPP Control Panel and start:

```text
Apache
MySQL
```

Then open:

```text
phpMyAdmin
```

Create/use the database:

```text
smartcommerce_analytics
```

---

## Step 3 – Configure Database

Update the database configuration in:

```text
python/config.py
```

The local setup used in this project is:

```text
Host     : localhost
Port     : 3306
User     : root
Password : ""
Database : smartcommerce_analytics
```

If your XAMPP MySQL installation uses a password, update the password accordingly.

---

# 21. Install Python Dependencies

Create/activate a Python environment if required and install:

```bash
pip install -r requirements.txt
```

The project requires libraries including:

```text
pandas
SQLAlchemy
PyMySQL
```

---

# 22. Execute SQL Tasks

Run the SQL files in sequence:

```text
sql/
├── 03_basic_queries.sql
├── 04_groupby_having.sql
├── 05_joins.sql
└── 06_integrity_checks.sql
```

They can be executed through phpMyAdmin's SQL interface.

---

# 23. Export the JOIN Result

From the project root:

```bash
python python/export_csv.py
```

The script connects to MySQL, executes the Task 4 JOIN and creates:

```text
output/reports/orders_customers_join.csv
```

Expected result:

```text
Rows    : 99441
Columns : 6
```

---

# 24. Run Data Cleaning

```bash
python python/data_cleaning.py
```

The script:

1. Loads the exported CSV.
2. Reports missing values and percentages.
3. Applies the defined imputation strategy if required.
4. Removes duplicate rows.
5. Saves the cleaned dataset.
6. Generates a cleaning report.

Output:

```text
data/cleaned/cleaned_orders.csv
```

---

# 25. Run Outlier Analysis

```bash
python python/outlier_analysis.py
```

The script loads `price` and `freight_value` from `order_items` and calculates:

- IQR outliers
- Z-score outliers

Report:

```text
output/reports/outlier_analysis_report.txt
```

---

# 26. Reproducibility

The complete workflow is:

```text
XAMPP MySQL/MariaDB
        ↓
smartcommerce_analytics database
        ↓
SQL extraction and validation
        ↓
Task 4 INNER JOIN
        ↓
orders_customers_join.csv
        ↓
Python / Pandas cleaning
        ↓
cleaned_orders.csv
        ↓
Outlier audit
        ↓
IQR + Z-score reports
```

This makes the Part 1 workflow reproducible from database extraction through data quality validation and outlier auditing.

---

# 27. Acceptance Criteria Mapping

The implementation is mapped to the Masai Part 1 acceptance criteria as follows:

| Masai Requirement | Project Evidence |
|---|---|
| Two-table relational dataset | `customers` and `orders` |
| Primary/foreign-key relationship | `customer_id` relationship |
| Six Task 2 SQL techniques | `sql/03_basic_queries.sql` |
| GROUP BY + HAVING | `sql/04_groupby_having.sql` |
| At least two aggregate functions | `COUNT`, `SUM`, `AVG` |
| INNER JOIN | `sql/05_joins.sql` |
| LEFT JOIN | `sql/05_joins.sql` |
| COUNT(DISTINCT) integrity check | `sql/06_integrity_checks.sql` |
| Grouped child-count check | `sql/06_integrity_checks.sql` |
| Orphan-row check | `sql/06_integrity_checks.sql` |
| JOIN exported to CSV | `python/export_csv.py` |
| CSV loaded in Pandas | `python/data_cleaning.py` |
| Missing count and percentage | Cleaning report |
| Imputation strategy | Mode for categorical, median for numeric |
| Duplicate count before/after | Cleaning report |
| Continuous numeric measures selected | `price`, `freight_value` |
| IQR method | `python/outlier_analysis.py` |
| Z-score method | `python/outlier_analysis.py` |
| IQR vs Z-score comparison | README and outlier report |
| Results documented | `output/reports/` |

---

# 28. Final Conclusion

Part 1 establishes a complete data-foundation workflow for the SmartCommerce business dataset.

The project successfully demonstrates:

- Relational database setup using **XAMPP MySQL/MariaDB**
- SQL filtering and retrieval
- Aggregation and group-level analysis
- Relational JOIN operations
- Referential-integrity validation
- CSV extraction
- Pandas-based data cleaning
- Missing-value auditing
- Duplicate detection
- Continuous-variable selection
- IQR-based outlier detection
- Z-score-based outlier detection
- Comparison of outlier detection methods
- Reproducible reporting

The final cleaned dataset contains:

```text
99,441 rows
6 columns
0 missing values
0 duplicate rows
```

The outlier audit covers:

```text
price
freight_value
```

using both:

```text
IQR
Z-score
```

This completes the SQL extraction, data-quality validation, cleaning and outlier-audit objectives of **Masai Capstone Part 1**.

---

## Author

**Bhuvaneswari Yennapusala**

