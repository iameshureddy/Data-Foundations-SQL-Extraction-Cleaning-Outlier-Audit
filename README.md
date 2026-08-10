# Data Foundations: SQL Extraction, Cleaning & Outlier Audit

**Capstone:** Part 1  
**Course:** Data Analytics with Gen & Agentic AI  
**Student:** Bhuvaneswari Yennapusala  
**Database:** MySQL through XAMPP / phpMyAdmin  
**Dataset:** Olist Brazilian E-Commerce Dataset

---

## 1. Project Overview

This project covers **Part 1 – Data Foundations: SQL Extraction, Cleaning & Outlier Audit**.

The project starts with the Olist Brazilian E-Commerce Dataset and loads the data into a relational MySQL database. SQL is used for filtering, aggregation, JOIN operations, and referential-integrity checks. A customer-order JOIN result is exported to CSV and processed using Python and Pandas. The final stage performs outlier analysis on continuous numeric business measures using both IQR and Z-score methods.

### Main work completed

- Relational database creation with primary and foreign keys
- SQL filtering using six required query types
- `GROUP BY` and `HAVING` analysis
- `INNER JOIN` and `LEFT JOIN`
- Referential-integrity validation
- JOIN result export to CSV
- Missing-value analysis
- Duplicate detection
- Data cleaning using Pandas
- IQR-based outlier detection
- Z-score-based outlier detection
- Comparison of IQR and Z-score results
- Reports and visualizations

---

## 2. Dataset

### Olist Brazilian E-Commerce Dataset

The project uses the Olist Brazilian E-Commerce Dataset.

The database contains the following main tables:

| Table | Description |
|---|---|
| `customers` | Customer information |
| `orders` | Order information |
| `products` | Product information |
| `order_items` | Items belonging to orders |
| `payments` | Payment information |
| `reviews` | Customer review information |

The main Part 1 analysis uses:

- `customers`
- `orders`
- `products`
- `payments`
- `order_items`
- `reviews`

---

## 3. Technology Used

| Technology | Purpose |
|---|---|
| MySQL | Relational database |
| XAMPP | Local MySQL server |
| phpMyAdmin | Database management and SQL execution |
| SQL | Data extraction and validation |
| Python | Data cleaning and analysis |
| Pandas | Data processing |
| NumPy | Numerical processing |
| SQLAlchemy | Python-MySQL connection |
| PyMySQL | MySQL driver |
| Matplotlib | Data visualization |
| Git | Version control |
| GitHub | Project repository |

---

# 4. Project Structure

```text
Data-Foundations-SQL-Extraction-Cleaning-Outlier-Audit/
│
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
│       └── cleaned_orders.csv
│
├── output/
│   └── reports/
│       ├── orders_customers_join.csv
│       ├── data_cleaning_report.txt
│       ├── outlier_analysis_report.txt
│       └── visualization_report.txt
│
├── images/
│   ├── monthly_orders.png
│   ├── orders_by_year.png
│   ├── orders_by_state.png
│   ├── top10_cities.png
│   ├── order_status_distribution.png
│   └── top_states_pie.png
│
├── requirements.txt
├── LICENSE
└── README.md
```

---

# 5. Database Design

Database name:

```text
smartcommerce_analytics
```

The database is created and managed locally using **XAMPP MySQL and phpMyAdmin**.

The schema uses primary keys and foreign-key relationships.

## Primary Keys

| Table | Primary Key |
|---|---|
| `customers` | `customer_id` |
| `orders` | `order_id` |
| `products` | `product_id` |
| `order_items` | `order_id`, `order_item_id` |
| `payments` | `order_id`, `payment_sequential` |
| `reviews` | `review_id` |

## Foreign Keys

| Child Table | Foreign Key | Parent Table |
|---|---|---|
| `orders` | `customer_id` | `customers.customer_id` |
| `order_items` | `order_id` | `orders.order_id` |
| `order_items` | `product_id` | `products.product_id` |
| `payments` | `order_id` | `orders.order_id` |
| `reviews` | `order_id` | `orders.order_id` |

## Main Relationship Used in Part 1

```text
customers (1) ─────── orders (1)

The relationship is:

```text
One Customer → Many Orders
```

The foreign-key relationship is:

```text
orders.customer_id
        ↓
customers.customer_id
```

---

# 6. Task 1 – Relational Database Setup

### Files

```text
database/01_schema.sql
database/02_import_data.sql
```

`01_schema.sql` creates the relational database structure.

`02_import_data.sql` is used to import the dataset into the database.

The schema contains multiple related tables and explicitly defines primary keys and foreign keys.

### Main relationship

```text
customers.customer_id
          ↓
orders.customer_id
```

This provides the relational structure required for the project.

---

# 7. Task 2 – Basic SQL Queries

### File

```text
sql/03_basic_queries.sql
```

The file contains the six required SQL query types.

## 7.1 WHERE ... IN

Find orders whose status is either delivered or shipped.

```sql
SELECT
    order_id,
    customer_id,
    order_status
FROM orders
WHERE order_status IN ('delivered','shipped');
```

## 7.2 WHERE ... NOT IN

The project uses `NOT IN` to exclude selected product categories.

```sql
SELECT
    product_id,
    product_category_name
FROM products
WHERE product_category_name NOT IN
(
    'bed_bath_table',
    'health_beauty',
    'sports_leisure'
);
```

## 7.3 BETWEEN

Find orders purchased during 2018.

```sql
SELECT
    order_id,
    customer_id,
    order_purchase_timestamp
FROM orders
WHERE order_purchase_timestamp
BETWEEN '2018-01-01 00:00:00'
AND '2018-12-31 23:59:59';
```

## 7.4 ORDER BY

Sort the result using two columns with different sorting directions.

```sql
SELECT
    order_id,
    product_id,
    price,
    freight_value
FROM order_items
ORDER BY
    price DESC,
    freight_value ASC;
```

Sorting:

```text
price         → DESC
freight_value → ASC
```

## 7.5 NOT EXISTS

Find customers for whom no order exists.

```sql
SELECT
    c.customer_id,
    c.customer_city,
    c.customer_state
FROM customers c
WHERE NOT EXISTS
(
    SELECT 1
    FROM orders o
    WHERE o.customer_id = c.customer_id
);
```

## 7.6 LIKE

Find customers living in cities containing `paulo`.

```sql
SELECT
    customer_id,
    customer_city,
    customer_state
FROM customers
WHERE customer_city LIKE '%paulo%';
```

---

# 8. Task 3 – GROUP BY and HAVING

### File

```text
sql/04_groupby_having.sql
```

The project groups payment information by payment type and calculates aggregate values.

The query uses:

```text
COUNT()
SUM()
AVG()
GROUP BY
HAVING
ORDER BY
```

Example:

```sql
SELECT
    p.payment_type,
    COUNT(*) AS total_transactions,
    SUM(p.payment_value) AS total_sales,
    AVG(p.payment_value) AS average_payment
FROM payments p
GROUP BY p.payment_type
HAVING SUM(p.payment_value) > 100000
ORDER BY total_sales DESC;
```

### Why HAVING is used

`WHERE` filters individual rows before grouping.

`HAVING` filters groups after aggregation.

In this project:

```sql
HAVING SUM(p.payment_value) > 100000
```

filters payment-type groups according to their total payment value.

---

# 9. Task 4 – JOIN Operations

**File:** `sql/05_joins.sql`

Task 4 demonstrates two SQL JOIN operations between the `customers` and `orders` tables.

The relationship is:

```text
customers (1) → orders (1)
```

The tables are joined using:

```text
customers.customer_id = orders.customer_id
```

## 9.1 INNER JOIN

The `INNER JOIN` retrieves customers who have matching orders.

Only records with a matching `customer_id` in both tables are returned. Customers without a matching order are excluded.

The query returns:

- Customer ID
- Customer city
- Customer state
- Order ID
- Order status

## 9.2 LEFT JOIN

The `LEFT JOIN` retrieves every customer, including customers who do not have a matching order.

The `customers` table is the **left table** because the objective is to retain every customer record. If a customer has no matching order, the order-related columns contain `NULL`.

The query returns:

- Customer ID
- Customer city
- Customer state
- Order ID
- Order status

## 9.3 Why are both JOINs used?

- **INNER JOIN:** retrieves only customers with matching orders.
- **LEFT JOIN:** retains all customers and includes order details when a match exists.

This demonstrates how the JOIN type is selected according to the analysis requirement.

---

# 10. Task 5 – Referential Integrity Validation

**File:** `sql/06_integrity_checks.sql`

Task 5 checks the relational integrity between the `customers` and `orders` tables.

The relationship is:

```text
One Customer → One Order in this dataset
```

The foreign-key relationship is:

```text
orders.customer_id → customers.customer_id
```

The `customers` table is the parent table and the `orders` table is the child table.

Three integrity checks are performed.

## 10.1 Matching Customer Count

`COUNT(DISTINCT)` is used to count unique customers having matching orders.

Observed result:

```text
99,441
```

## 10.2 Customers with More Than One Order

`GROUP BY` and `HAVING COUNT()` are used to identify customers with more than one order.

Observed result:

```text
0 rows
```

## 10.3 Orphan Order Check

A `LEFT JOIN` is used to identify orders whose `customer_id` does not exist in the `customers` table.

Observed result:

```text
0 rows
```

## 10.4 Task 5 Result

| Integrity Check | Result |
|---|---:|
| Customers with matching orders | 99,441 |
| Customers with more than one order | 0 rows |
| Orphan orders | 0 rows |

These checks provide evidence that the loaded customer-order relationship contains no orphan orders and that the expected customer-order relationship is being maintained in the analysis.

---

# 11. Task 6 – Export JOIN Result to CSV

### File

```text
python/export_csv.py
```

The customer-order JOIN result from Task 4 is exported from MySQL into a CSV file.

### Output

```text
output/reports/orders_customers_join.csv
```

### Exported columns

```text
customer_id
customer_city
customer_state
order_id
order_status
order_purchase_timestamp
```

### Observed result

```text
Rows    : 99,441
Columns : 6
```

The exported CSV is used as the input for Task 7.

---

# 12. Task 7 – Data Cleaning

### File

```text
python/data_cleaning.py
```

### Input

```text
output/reports/orders_customers_join.csv
```

### Output

```text
data/cleaned/cleaned_orders.csv
```

### Report

```text
output/reports/data_cleaning_report.txt
```

## 12.1 Missing Values

The script checks both the number and percentage of missing values.

Observed result:

| Column | Missing Values | Percentage |
|---|---:|---:|
| `customer_id` | 0 | 0.0% |
| `customer_city` | 0 | 0.0% |
| `customer_state` | 0 | 0.0% |
| `order_id` | 0 | 0.0% |
| `order_status` | 0 | 0.0% |
| `order_purchase_timestamp` | 0 | 0.0% |

Total missing values:

```text
0
```

No missing values remained after cleaning.

## 12.2 Missing-Value Treatment

The Python script contains an explicit treatment strategy:

```text
Categorical/object columns → Mode
Numeric columns            → Median
```

The actual dataset contained no missing values, so no rows required imputation during this run.

The strategy is included in the code so that the cleaning process can handle missing values if they are present.

## 12.3 Duplicate Check

Observed result:

```text
Rows before cleaning           : 99,441
Rows after cleaning            : 99,441
Duplicate rows removed         : 0
Duplicate rows after removal   : 0
```

### Final cleaned dataset

```text
Rows             : 99,441
Columns          : 6
Missing values   : 0
Duplicate rows   : 0
```

---

# 13. Task 8 – Outlier Audit

### File

```text
python/outlier_analysis.py
```

### Report

```text
output/reports/outlier_analysis_report.txt
```

The outlier audit is performed on continuous numeric business measures from the `order_items` table.

## 13.1 Continuous Numeric Measure Filtering Rule

Only continuous numeric business measures are included in the outlier audit.

Identifier and key columns are excluded because their numeric values represent labels rather than measurements. Binary or flag columns and zero or near-zero variance columns are also excluded because they are not meaningful continuous measures.

The selected continuous numeric measures are:

- `price`
- `freight_value`

The analysis is performed directly on the MySQL `order_items` table because the CSV exported for Task 6 contains customer and order fields but does not contain `price` or `freight_value`.

### Rows analysed

```text
112,650
```

---

# 14. IQR Method

The Interquartile Range method uses:

```text
IQR = Q3 - Q1

Lower Fence = Q1 - 1.5 × IQR
Upper Fence = Q3 + 1.5 × IQR
```

A value below the lower fence or above the upper fence is classified as an outlier.

## 14.1 Price

| Metric | Value |
|---|---:|
| Q1 | 39.900000 |
| Q3 | 134.900000 |
| IQR | 95.000000 |
| Lower Fence | -102.600000 |
| Upper Fence | 277.400000 |
| Outliers | 8,427 |

## 14.2 Freight Value

| Metric | Value |
|---|---:|
| Q1 | 13.080000 |
| Q3 | 21.150000 |
| IQR | 8.070000 |
| Lower Fence | 0.975000 |
| Upper Fence | 33.255000 |
| Outliers | 12,134 |

---

# 15. Z-score Method

The Z-score is calculated as:

```text
Z = (value - mean) / standard deviation
```

The project uses:

```text
|Z| > 3
```

as the outlier threshold.

## 15.1 Price

| Metric | Value |
|---|---:|
| Mean | 120.653739 |
| Standard deviation | 183.633928 |
| Z threshold | 3 |
| Outliers | 1,966 |

## 15.2 Freight Value

| Metric | Value |
|---|---:|
| Mean | 19.990320 |
| Standard deviation | 15.806405 |
| Z threshold | 3 |
| Outliers | 2,041 |

---

# 16. IQR vs Z-score Comparison

| Measure | IQR Outliers | Z-score Outliers | Difference | Result |
|---|---:|---:|---:|---|
| `price` | 8,427 | 1,966 | 6,461 | Disagree |
| `freight_value` | 12,134 | 2,041 | 10,093 | Disagree |

## Why are the results different?

IQR is based on quartiles and is generally more robust to skewed data and extreme values.

Z-score depends on the mean and standard deviation and is most appropriate when the data are approximately normally distributed.

Because the two methods use different rules for identifying unusual values, they can produce different outlier counts.

In this dataset, the IQR method identifies substantially more outliers than the Z-score method for both selected measures.

---

# 17. Reports and Outputs

| File | Purpose |
|---|---|
| `output/reports/orders_customers_join.csv` | Task 6 JOIN result |
| `data/cleaned/cleaned_orders.csv` | Task 7 cleaned dataset |
| `output/reports/data_cleaning_report.txt` | Task 7 results |
| `output/reports/outlier_analysis_report.txt` | Task 8 results |
| `output/reports/visualization_report.txt` | Visualization information |

---

# 18. Visualizations

The project includes generated visualizations stored directly inside the `images/` directory.

### Monthly Orders

![Monthly Orders](images/monthly_orders.png)

### Orders by Year

![Orders by Year](images/orders_by_year.png)

### Orders by State

![Orders by State](images/orders_by_state.png)

### Top 10 Cities

![Top 10 Cities](images/top10_cities.png)

### Order Status Distribution

![Order Status Distribution](images/order_status_distribution.png)

### Top States

![Top States](images/top_states_pie.png)

These charts provide supporting visual evidence for the analysis.

---

# 19. How to Run the Project

## Step 1 – Clone the repository

```bash
git clone https://github.com/iameshureddy/Data-Foundations-SQL-Extraction-Cleaning-Outlier-Audit.git
cd Data-Foundations-SQL-Extraction-Cleaning-Outlier-Audit
```

## Step 2 – Start XAMPP

Open the XAMPP Control Panel and start:

```text
MySQL
```

Open phpMyAdmin:

```text
http://localhost/phpmyadmin/
```

The Python database configuration uses:

```text
Host     : localhost
Port     : 3306
User     : root
Password : empty
Database : smartcommerce_analytics
```

If your local MySQL installation uses a password, update the database configuration before running the Python scripts.

## Step 3 – Install Python dependencies

```bash
python -m pip install -r requirements.txt
```

## Step 4 – Create the database

Open phpMyAdmin and execute:

```text
database/01_schema.sql
```

## Step 5 – Import the data

Execute:

```text
database/02_import_data.sql
```

## Step 6 – Run the SQL tasks

Execute the following files in phpMyAdmin:

```text
sql/03_basic_queries.sql
sql/04_groupby_having.sql
sql/05_joins.sql
sql/06_integrity_checks.sql
```

## Step 7 – Export the JOIN result

From the project root:

```powershell
python python/export_csv.py
```

## Step 8 – Run data cleaning

```powershell
python python/data_cleaning.py
```

## Step 9 – Run outlier analysis

```powershell
python python/outlier_analysis.py
```

## Step 10 – Generate visualizations

```powershell
python python/generate_visualizations.py
```

---

# 20. Part 1 Checklist

| Task | Work completed | File / Output |
|---|---|---|
| Task 1 | Created relational database with primary and foreign keys | `database/01_schema.sql` |
| Task 2 | Added the six required SQL query types | `sql/03_basic_queries.sql` |
| Task 3 | Used `GROUP BY`, `HAVING`, `COUNT`, `SUM`, and `AVG` | `sql/04_groupby_having.sql` |
| Task 4 | Added `INNER JOIN` and `LEFT JOIN` with explanations | `sql/05_joins.sql` |
| Task 5 | Checked matching customers, grouped orders, and orphan orders | `sql/06_integrity_checks.sql` |
| Task 6 | Exported the customer-order JOIN result | `orders_customers_join.csv` |
| Task 7 | Checked missing values and duplicates and created a cleaned dataset | `python/data_cleaning.py` |
| Task 8 | Analysed `price` and `freight_value` using IQR and Z-score | `python/outlier_analysis.py` |
| Reports | Saved cleaning and outlier results | `output/reports/` |
| Visualizations | Generated charts from the project data | `images/` |
| Documentation | Added setup and execution instructions | `README.md` |

---

# 21. Part 1 Acceptance Criteria

The following table maps the Part 1 requirements to the files, reports, and outputs in the repository.

| Acceptance criterion | Evidence in project | Status |
|---|---|---|
| Relational database with primary and foreign-key relationships | `database/01_schema.sql` | Completed |
| Six required SQL query types | `sql/03_basic_queries.sql` | Completed |
| `GROUP BY` with aggregate functions | `sql/04_groupby_having.sql` | Completed |
| `HAVING` filtering after aggregation | `sql/04_groupby_having.sql` | Completed |
| `INNER JOIN` | `sql/05_joins.sql` | Completed |
| `LEFT JOIN` | `sql/05_joins.sql` | Completed |
| JOIN purpose and choice documented | `sql/05_joins.sql` and README | Completed |
| `COUNT(DISTINCT)` integrity check | `sql/06_integrity_checks.sql` | Completed |
| Grouped child-count integrity check | `sql/06_integrity_checks.sql` | Completed |
| Orphan-record integrity check | `sql/06_integrity_checks.sql` | Completed |
| JOIN result exported to CSV | `output/reports/orders_customers_join.csv` | Completed |
| CSV loaded using Pandas | `python/data_cleaning.py` | Completed |
| Missing-value counts and percentages | `output/reports/data_cleaning_report.txt` | Completed |
| Explicit missing-value treatment strategy | `python/data_cleaning.py` | Completed |
| Missing values after cleaning | Cleaning report | 0 |
| Duplicate count before and after cleaning | Cleaning report | Completed |
| Continuous numeric measure filtering | `python/outlier_analysis.py` | Completed |
| IQR outlier detection | Outlier analysis report | Completed |
| Z-score outlier detection | Outlier analysis report | Completed |
| IQR bounds documented | Outlier analysis report | Completed |
| Z-score threshold documented | Outlier analysis report | Completed |
| Results for every selected measure | `price`, `freight_value` | Completed |
| IQR versus Z-score comparison | Outlier analysis report | Completed |
| Explanation of method differences | README and outlier report | Completed |
| README documents schema and workflow | `README.md` | Completed |

The checklist is included as a quick reference. The SQL files, Python scripts, and generated reports contain the detailed implementation and results.

---

# 22. Final Results

## Database and JOIN

```text
Database    : smartcommerce_analytics
JOIN rows   : 99,441
JOIN columns: 6
```

## Referential Integrity

```text
Matching customers      : 99,441
Customers with >1 order : 0 rows
Orphan orders            : 0 rows
```

## Data Cleaning

```text
Rows before cleaning : 99,441
Rows after cleaning  : 99,441
Duplicates removed   : 0
Missing values       : 0
```

## Outlier Analysis

```text
price
    IQR outliers     : 8,427
    Z-score outliers : 1,966

freight_value
    IQR outliers     : 12,134
    Z-score outliers : 2,041
```

---

# 23. Conclusion

The project follows the Part 1 workflow from relational database creation to data-quality analysis:

```text
Olist Dataset
      ↓
MySQL / XAMPP
      ↓
SQL Queries
      ↓
GROUP BY / HAVING
      ↓
INNER JOIN / LEFT JOIN
      ↓
Referential Integrity
      ↓
CSV Export
      ↓
Pandas Data Cleaning
      ↓
IQR / Z-score Outlier Audit
      ↓
Reports and Visualizations
```

The implementation demonstrates SQL-based data extraction and validation together with Python-based data cleaning and statistical outlier analysis.
