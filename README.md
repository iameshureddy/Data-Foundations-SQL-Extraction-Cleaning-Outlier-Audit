# Data Foundations: SQL Extraction, Cleaning & Outlier Audit

**Capstone:** Part 1
**Course:** Data Analytics with Gen & Agentic AI
**Student:** Bhuvaneswari Yennapusala
**Database:** MySQL through XAMPP / phpMyAdmin
**Dataset:** Olist Brazilian E-Commerce Dataset

---

## 1. Project Overview

This project covers **Part 1 – Data Foundations: SQL Extraction, Cleaning & Outlier Audit**.

The project starts with the Olist Brazilian E-Commerce dataset and loads the data into a relational MySQL database. SQL is then used for filtering, aggregation, JOIN operations, and referential-integrity checks. A customer-order JOIN result is exported to CSV and processed with Python and Pandas. The final stage performs outlier analysis on continuous numeric business measures using both IQR and Z-score methods.

### Main work completed

- Relational database creation with primary and foreign keys
- SQL filtering using six required query types
- `GROUP BY` and `HAVING` analysis
- `INNER JOIN` and `LEFT JOIN`
- Referential-integrity validation
- JOIN result export to CSV
- Missing-value and duplicate analysis
- Data cleaning using Pandas
- IQR-based outlier detection
- Z-score-based outlier detection
- Comparison of the two outlier methods
- Reports and visualizations

---

## 2. Dataset

### Olist Brazilian E-Commerce Dataset

The project uses the Olist Brazilian E-Commerce dataset, which contains relational e-commerce information.

The database includes the following tables:

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
- `payments`
- `order_items`

---

## 3. Technology Used

| Technology | Purpose |
|---|---|
| MySQL | Relational database |
| XAMPP | Local MySQL server |
| phpMyAdmin | Database management and SQL execution |
| SQL | Data extraction and validation |
| Python | Cleaning and statistical analysis |
| Pandas | Data processing |
| NumPy | Numerical processing |
| SQLAlchemy | Python-MySQL connection |
| PyMySQL | MySQL driver |
| Matplotlib | Visualizations |
| Git | Version control |
| GitHub | Project repository |

---

## 4. Project Structure

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

The schema uses primary keys and foreign-key constraints.

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

| Child table | Foreign key | Parent table |
|---|---|---|
| `orders` | `customer_id` | `customers.customer_id` |
| `order_items` | `order_id` | `orders.order_id` |
| `order_items` | `product_id` | `products.product_id` |
| `payments` | `order_id` | `orders.order_id` |
| `reviews` | `order_id` | `orders.order_id` |

## Main Relationship Used in Part 1

```text
customers (1) ───────< orders (M)
```

The relationship is:

```text
One Customer → Many Orders
```

with:

```text
orders.customer_id
        ↓
customers.customer_id
```

The database schema enforces the relationship through a foreign-key constraint.

---

# 6. Task 1 – Relational Database Setup

### Files

```text
database/01_schema.sql
database/02_import_data.sql
```

`01_schema.sql` creates the database tables and their relationships.

`02_import_data.sql` is used to load the dataset.

The schema contains multiple related tables and explicitly defines primary and foreign keys.

### Main relationship

```text
customers.customer_id
          ↓
orders.customer_id
```

This gives the database a real relational structure instead of treating each dataset as an independent file.

---

# 7. Task 2 – Basic SQL Queries

### File

```text
sql/03_basic_queries.sql
```

The file contains the six required SQL query types.

## 7.1 WHERE ... IN

Find delivered or shipped orders:

```sql
SELECT
    order_id,
    customer_id,
    order_status
FROM orders
WHERE order_status IN ('delivered','shipped');
```

## 7.2 WHERE ... NOT IN

The project uses `NOT IN` to exclude selected product categories:

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

Find orders purchased during the required date range:

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

Sort by two columns:

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

This demonstrates:

```text
price         → DESC
freight_value → ASC
```

## 7.5 NOT EXISTS

Find customers for whom no order exists:

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

Find customers whose city contains `paulo`:

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

The project groups payment information by payment type and calculates multiple aggregate values.

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

### Why `HAVING` is used

`WHERE` filters individual rows before grouping.

`HAVING` filters the groups after aggregation.

Here:

```sql
HAVING SUM(p.payment_value) > 100000
```

keeps only payment-type groups whose total value is above the selected threshold.

---

# 9. Task 4 – JOIN Operations

### File

```text
sql/05_joins.sql
```

This file demonstrates both:

```text
INNER JOIN
LEFT JOIN
```

between:

```text
customers
orders
```

The relationship used is:

```text
orders.customer_id
        ↓
customers.customer_id
```

## 9.1 INNER JOIN

```sql
SELECT
    c.customer_id,
    c.customer_city,
    c.customer_state,
    o.order_id,
    o.order_status
FROM customers AS c
INNER JOIN orders AS o
    ON c.customer_id = o.customer_id
ORDER BY
    o.order_id ASC;
```

### Why INNER JOIN?

The INNER JOIN is used when only customers with matching orders are required.

Records without a matching `customer_id` in the other table are not included.

---

## 9.2 LEFT JOIN

```sql
SELECT
    c.customer_id,
    c.customer_city,
    c.customer_state,
    o.order_id,
    o.order_status
FROM customers AS c
LEFT JOIN orders AS o
    ON c.customer_id = o.customer_id
ORDER BY
    c.customer_state ASC,
    c.customer_city ASC;
```

### Why LEFT JOIN?

The `customers` table is placed on the left because the purpose is to retain **every customer**, including customers who do not have a matching order.

When a customer has no matching order, the order-related columns can contain `NULL`.

This makes the LEFT JOIN useful for checking whether customer records without orders exist.

---

# 10. Task 5 – Referential Integrity Validation

### File

```text
sql/06_integrity_checks.sql
```

The main relationship checked in this task is:

```text
Parent Table : customers
Child Table  : orders

Relationship : One-to-Many (1:M)

Foreign Key:
orders.customer_id → customers.customer_id
```

Three checks are performed.

## 10.1 Matching customer count

```sql
SELECT
    COUNT(DISTINCT c.customer_id) AS unique_customers
FROM customers AS c
INNER JOIN orders AS o
    ON c.customer_id = o.customer_id;
```

This counts the distinct customers that have matching orders.

Observed result:

```text
99,441
```

## 10.2 Customers with more than one order

```sql
SELECT
    o.customer_id,
    COUNT(o.order_id) AS total_orders
FROM orders AS o
GROUP BY o.customer_id
HAVING COUNT(o.order_id) > 1
ORDER BY total_orders DESC;
```

This checks whether any customer has multiple order records under the loaded `customer_id` relationship.

Observed result:

```text
0 rows
```

The query is still useful as a validation of the expected one-to-many relationship even though this particular extracted dataset did not return customers with more than one order.

## 10.3 Orphan-order check

```sql
SELECT
    o.order_id,
    o.customer_id
FROM orders AS o
LEFT JOIN customers AS c
    ON o.customer_id = c.customer_id
WHERE c.customer_id IS NULL;
```

Observed result:

```text
0 rows
```

This means no order was found whose `customer_id` was missing from the `customers` table.

### Task 5 result

```text
Customers with matching orders : 99,441
Customers with >1 order        : 0 rows
Orphan orders                  : 0 rows
```

---

# 11. Task 6 – Export JOIN Result to CSV

### File

```text
python/export_csv.py
```

The Task 4 customer-order JOIN is exported from MySQL to CSV.

### Output

```text
output/reports/orders_customers_join.csv
```

### Exported fields

```text
customer_id
customer_city
customer_state
order_id
order_status
order_purchase_timestamp
```

### Observed output

```text
Rows    : 99,441
Columns : 6
```

The CSV is then used as the input for Task 7.

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

### Cleaned output

```text
data/cleaned/cleaned_orders.csv
```

### Report

```text
output/reports/data_cleaning_report.txt
```

## Missing-value analysis

The script calculates both the number and percentage of missing values for every column.

Observed result:

| Column | Missing | Percentage |
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

## Missing-value treatment

The code uses:

```text
Categorical/object columns → Mode
Numeric columns            → Median
```

The strategy is defined even though the actual dataset did not contain missing values.

Median is less affected by extreme values than the mean, while mode is suitable for categorical values.

## Duplicate check

Observed result:

```text
Rows before cleaning : 99,441
Rows after cleaning  : 99,441
Duplicates removed   : 0
```

### Final cleaned dataset

```text
Rows           : 99,441
Columns        : 6
Missing values : 0
Duplicates     : 0
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

The analysis uses continuous numeric business measures from `order_items`.

Selected measures:

```text
price
freight_value
```

Rows analysed:

```text
112,650
```

## Continuous numeric filtering

The analysis is designed to exclude:

- identifier/key columns
- binary/flag columns
- zero or near-zero variance columns

The final selected continuous business measures are:

```text
price
freight_value
```

---

## 13.1 IQR Method

The project uses:

```text
Q1 = 25th percentile
Q3 = 75th percentile

IQR = Q3 - Q1

Lower Fence = Q1 - 1.5 × IQR
Upper Fence = Q3 + 1.5 × IQR
```

### Price

| Metric | Value |
|---|---:|
| Q1 | 39.900000 |
| Q3 | 134.900000 |
| IQR | 95.000000 |
| Lower Fence | -102.600000 |
| Upper Fence | 277.400000 |
| Outliers | 8,427 |

### Freight value

| Metric | Value |
|---|---:|
| Q1 | 13.080000 |
| Q3 | 21.150000 |
| IQR | 8.070000 |
| Lower Fence | 0.975000 |
| Upper Fence | 33.255000 |
| Outliers | 12,134 |

---

# 14. Z-score Method

The Z-score is calculated as:

```text
Z = (value - mean) / standard deviation
```

The project uses:

```text
|Z| > 3
```

as the outlier threshold.

## Price

| Metric | Value |
|---|---:|
| Mean | 120.653739 |
| Standard deviation | 183.633928 |
| Z threshold | 3 |
| Outliers | 1,966 |

## Freight value

| Metric | Value |
|---|---:|
| Mean | 19.990320 |
| Standard deviation | 15.806405 |
| Z threshold | 3 |
| Outliers | 2,041 |

---

# 15. IQR and Z-score Comparison

| Measure | IQR outliers | Z-score outliers | Difference | Result |
|---|---:|---:|---:|---|
| `price` | 8,427 | 1,966 | 6,461 | Disagree |
| `freight_value` | 12,134 | 2,041 | 10,093 | Disagree |

### Why are the results different?

The IQR method is based on quartiles and is generally more robust when data are skewed or contain extreme values.

The Z-score method depends on the mean and standard deviation and is more suitable when the data are approximately normally distributed.

Because the two methods use different definitions of an outlier, they can identify different observations.

---

# 16. Reports and Outputs

| Output | Purpose |
|---|---|
| `orders_customers_join.csv` | Task 6 JOIN export |
| `data_cleaning_report.txt` | Task 7 cleaning results |
| `outlier_analysis_report.txt` | Task 8 outlier results |
| `cleaned_orders.csv` | Cleaned Task 6 dataset |
| `visualization_report.txt` | Visualization information |

---

# 17. Visualizations

The project also contains visualizations generated from the order data.

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

These visualizations are included as supporting evidence for the exploratory analysis.

---

# 18. How to Run the Project

## Step 1 – Clone the repository

```bash
git clone https://github.com/iameshureddy/Data-Foundations-SQL-Extraction-Cleaning-Outlier-Audit.git
cd Data-Foundations-SQL-Extraction-Cleaning-Outlier-Audit
```

## Step 2 – Start XAMPP

Open XAMPP Control Panel and start:

```text
MySQL
```

Open phpMyAdmin:

```text
http://localhost/phpmyadmin/
```

The Python scripts use the following local configuration:

```text
Host     : localhost
Port     : 3306
User     : root
Password : empty
Database : smartcommerce_analytics
```

If your XAMPP MySQL installation has a password, update the Python database configuration before running the scripts.

## Step 3 – Install Python packages

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

Run these files in phpMyAdmin:

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

# 19. Part 1 Checklist

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

# 20. Final Results

### Database and JOIN

```text
Database : smartcommerce_analytics
JOIN rows: 99,441
JOIN columns: 6
```

### Referential integrity

```text
Matching customers : 99,441
Customers with >1 order : 0 rows
Orphan orders : 0 rows
```

### Data cleaning

```text
Rows before cleaning : 99,441
Rows after cleaning  : 99,441
Duplicates removed   : 0
Missing values       : 0
```

### Outlier analysis

```text
price
    IQR outliers     : 8,427
    Z-score outliers : 1,966

freight_value
    IQR outliers     : 12,134
    Z-score outliers : 2,041
```

---

# 21. Conclusion

Part 1 provides a complete workflow from relational data storage to data-quality analysis:

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
Pandas Cleaning
      ↓
IQR / Z-score Outlier Audit
      ↓
Reports and Visualizations
```

The project demonstrates the use of SQL for relational data analysis and Python for data preparation and statistical outlier detection.

---

# 22. Repository

GitHub repository:

https://github.com/iameshureddy/Data-Foundations-SQL-Extraction-Cleaning-Outlier-Audit
