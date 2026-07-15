# 📊 Data Foundations: SQL Extraction, Cleaning & Outlier Audit

> **Data Analytics with Gen & Agentic AI – Capstone Project (Part 1)**

![Python](https://img.shields.io/badge/Python-3.12-blue)
![MySQL](https://img.shields.io/badge/MySQL-MariaDB-orange)
![Pandas](https://img.shields.io/badge/Pandas-2.3.3-brightgreen)
![NumPy](https://img.shields.io/badge/NumPy-1.26.4-blue)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0.51-red)
![License](https://img.shields.io/badge/License-Educational-success)

---

# 👩‍💻 Author

**Bhuvaneswari Yennapusala**

B.Tech – Computer Engineering (Artificial Intelligence)

Masai School – Data Analytics with Gen & Agentic AI

---

# 📖 Project Overview

This project demonstrates a complete **SQL-based data analytics workflow** using the **Olist Brazilian E-Commerce Public Dataset**. It focuses on building a reliable data foundation by integrating SQL and Python to perform database design, data extraction, data validation, cleaning, and statistical analysis.

The workflow begins with designing a normalized relational database in MySQL, followed by importing six interconnected datasets. SQL is then used to extract meaningful business information, perform aggregation, validate referential integrity, and join relational tables. The extracted data is exported to CSV and further processed using Python for data cleaning, duplicate analysis, and statistical outlier detection.

To enhance analytical understanding, automated visualizations are generated using Matplotlib, producing reproducible charts directly from code. The final output includes cleaned datasets, analysis reports, and visualizations suitable for downstream analytics and machine learning tasks.

This project demonstrates practical skills in **database management, SQL querying, Python data processing, statistical auditing, and reproducible analytics workflows**, following industry-standard data engineering practices.

---

# 🎯 Project Objectives

The primary objectives of this project are:

- Design a normalized relational database.
- Import structured business datasets into MySQL.
- Perform SQL-based data extraction and filtering.
- Analyze data using GROUP BY and HAVING clauses.
- Implement SQL JOIN operations across multiple tables.
- Validate referential integrity between related tables.
- Export relational data for further processing.
- Clean and preprocess data using Python.
- Detect missing values and duplicate records.
- Identify statistical outliers using IQR and Z-Score methods.
- Generate automated visualizations for exploratory analysis.
- Produce reproducible reports suitable for future analytical workflows.

---

# ✨ Project Features

- ✔ Relational database design with normalized tables
- ✔ SQL-based business query implementation
- ✔ Automated CSV export from MySQL
- ✔ Python-based data cleaning pipeline
- ✔ Missing value and duplicate analysis
- ✔ Statistical outlier detection
- ✔ Automated visualization generation
- ✔ Report generation for every analysis stage
- ✔ Clean and reproducible project structure
- ✔ Ready for further Business Intelligence and Machine Learning applications

---

# 📂 Dataset

## Dataset Used

**Olist Brazilian E-Commerce Public Dataset**

The Olist dataset is a publicly available Brazilian e-commerce dataset containing transactional information collected from a large online marketplace. It consists of multiple related tables representing customers, products, orders, payments, reviews, and purchased items.

The dataset is well suited for demonstrating relational database concepts because the tables are connected through primary and foreign key relationships.

### Imported Tables

| Table | Description |
|---------|-------------|
| customers | Customer information including city and state |
| orders | Order lifecycle information |
| products | Product catalogue |
| order_items | Purchased products within each order |
| payments | Payment transactions for each order |
| reviews | Customer review information |

### Dataset Characteristics

- Multi-table relational dataset
- More than **500,000 records** across all imported tables
- Contains customer, transactional, and product information
- Includes timestamp columns for time-based analysis
- Suitable for SQL joins and integrity validation

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|----------|
| MySQL / MariaDB | Relational Database Management |
| SQL | Data Definition & Query Language |
| Python 3.12 | Data Processing |
| Pandas | Data Cleaning & Analysis |
| NumPy | Numerical Computation |
| SQLAlchemy | Database Connectivity |
| PyMySQL | MySQL Driver |
| Matplotlib | Data Visualization |
| VS Code | Development Environment |
| Git & GitHub | Version Control |

---

# 📁 Project Structure

```text
Data-Foundations-SQL-Extraction-Cleaning-Outlier-Audit/

│
├── database/
│   ├── 01_schema.sql
│   ├── 02_import_data.sql
│   └── database_design.md
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
│   │   ├── olist_customers_dataset.csv
│   │   ├── olist_orders_dataset.csv
│   │   ├── olist_products_dataset.csv
│   │   ├── olist_order_items_dataset.csv
│   │   ├── olist_order_payments_dataset.csv
│   │   └── olist_order_reviews_dataset.csv
│   │
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
│   └── plots/
│       ├── monthly_orders.png
│       ├── orders_by_year.png
│       ├── orders_by_state.png
│       ├── order_status_distribution.png
│       ├── top10_cities.png
│       └── top_states_pie.png
│
├── requirements.txt
├── LICENSE
├── README.md
└── .gitignore
```

---

# 🗄️ Database Design

## Database Name

```sql
smartcommerce_analytics
```

The database was designed using a normalized relational schema to efficiently manage customer, order, product, payment, and review information while maintaining referential integrity.

---

## Database Tables

The project contains six relational tables:

| Table | Purpose |
|---------|----------|
| customers | Stores customer information |
| orders | Stores order details |
| products | Stores product information |
| order_items | Maps products to orders |
| payments | Stores payment information |
| reviews | Stores customer reviews |

---

## Primary Keys

| Table | Primary Key |
|---------|-------------|
| customers | customer_id |
| orders | order_id |
| products | product_id |
| order_items | (order_id, order_item_id) |
| payments | (order_id, payment_sequential) |
| reviews | review_id |

---

## Foreign Key Relationships

| Parent Table | Child Table |
|---------------|-------------|
| customers | orders |
| orders | order_items |
| products | order_items |
| orders | payments |
| orders | reviews |

---

## Entity Relationship Overview

The relational model follows database normalization principles.

Relationship summary:

- One customer can place multiple orders.
- One order can contain multiple purchased products.
- Products are connected to orders through the **order_items** table.
- Each order may have one or more payment records.
- Customers can submit reviews for completed orders.

This structure minimizes redundancy while maintaining efficient query performance and referential integrity.

---

# ✅ Task 1 – Database Design

## Objective

The first step of this project was to design a normalized relational database capable of storing the Olist Brazilian E-Commerce dataset while preserving data consistency and referential integrity.

A well-designed relational database improves data organization, reduces redundancy, and enables efficient querying across multiple related tables.

---

### Implementation

The following tasks were completed:

- Created the `smartcommerce_analytics` database.
- Designed six relational tables based on the Olist dataset.
- Defined Primary Keys for unique record identification.
- Established Foreign Key relationships between related tables.
- Maintained referential integrity across all tables.
- Normalized the database to minimize data redundancy.

---

### Database Tables

| Table | Purpose |
|---------|----------|
| customers | Stores customer information |
| orders | Stores customer orders |
| products | Stores product catalogue |
| order_items | Connects products with orders |
| payments | Stores payment transactions |
| reviews | Stores customer review information |

---

### Outcome

A fully normalized relational database was successfully created and prepared for importing the original Olist dataset.

---

### Files Used

```
database/01_schema.sql

database/database_design.md
```

---

### Screenshot

> Add:

- Database ER Diagram
- Database Structure (phpMyAdmin)
- Tables Created Successfully

---

# ✅ Task 2 – SQL Data Extraction

## Objective

The objective of this task was to retrieve meaningful business information from the relational database using SQL queries.

Different SQL filtering techniques were applied to analyze customer, product, and order data efficiently.

---

## SQL Concepts Implemented

The following SQL operations were used throughout the project:

- WHERE
- IN
- NOT IN
- BETWEEN
- LIKE
- ORDER BY
- LIMIT
- EXISTS
- NOT EXISTS

---

## Sample Business Questions Solved

Examples include:

- Retrieve delivered orders.
- Find customers belonging to specific states.
- Search products using pattern matching.
- Filter orders placed within a date range.
- Identify records that do not satisfy specific conditions.
- Sort customers alphabetically.
- Display limited analytical results.

---

## Learning Outcome

These SQL filtering techniques enable efficient extraction of business information while minimizing unnecessary data retrieval.

---

### Files Used

```
sql/03_basic_queries.sql
```

---

### Screenshot

> Add:

- SQL Query Results
- WHERE Query
- LIKE Query
- BETWEEN Query

---

# ✅ Task 3 – GROUP BY & HAVING

## Objective

This task focuses on performing analytical queries using SQL aggregation functions.

Grouping operations summarize large datasets into meaningful business insights.

---

## Aggregate Functions Used

The following aggregate functions were implemented:

- COUNT()
- SUM()
- AVG()
- MIN()
- MAX()

---

## GROUP BY

The GROUP BY clause was used to summarize data based on common attributes such as customer location and order status.

Examples include:

- Number of customers per state
- Total orders by status
- Average product price
- Total payments received

---

## HAVING

The HAVING clause was used to filter grouped results after aggregation.

Examples include:

- States having more than a specified number of customers.
- Order statuses with high transaction counts.
- Groups exceeding average business thresholds.

---

## Learning Outcome

Using GROUP BY together with aggregate functions enables quick business summarization, while HAVING filters aggregated results based on analytical conditions.

---

### Files Used

```
sql/04_groupby_having.sql
```

---

### Screenshot

> Add:

- GROUP BY Output
- HAVING Output

---

# ✅ Task 4 – SQL Joins

## Objective

The objective of this task was to combine data stored across multiple relational tables using SQL JOIN operations.

Since business information is distributed across different entities, joins are essential for producing meaningful analytical datasets.

---

## INNER JOIN

An INNER JOIN retrieves only records that have matching values in both tables.

### Implementation

Customers were joined with orders using:

```
customers.customer_id = orders.customer_id
```

This produced a dataset containing customers who successfully placed orders.

---

## LEFT JOIN

A LEFT JOIN returns all records from the left table and matching records from the right table.

It is particularly useful for identifying missing relationships such as customers who have not placed any orders.

---

## Why JOINs Are Important

JOIN operations enable analysts to combine information stored in different relational tables without data duplication.

They are widely used in reporting, dashboards, business intelligence, and analytics workflows.

---

## CSV Export

The final INNER JOIN result was exported automatically using Python.

Generated output:

```
output/reports/orders_customers_join.csv
```

This exported dataset serves as the input for subsequent data cleaning and outlier analysis.

---

### Files Used

```
sql/05_joins.sql

python/export_csv.py
```

---

### Output

Generated file:

```
orders_customers_join.csv
```

Rows Exported:

```
99,441
```

Columns Exported:

```
6
```

---

### Screenshot

> Add:

- INNER JOIN Query
- JOIN Output
- CSV Export Terminal Output

---

# ✅ Task 5 – Referential Integrity Validation

## Objective

The objective of this task was to verify the consistency and integrity of relationships between the imported tables.

Referential integrity ensures that every foreign key value corresponds to an existing primary key, preventing orphan records and maintaining database accuracy.

---

## Validation Performed

The following integrity checks were implemented:

- Parent–Child Relationship Validation
- Foreign Key Verification
- COUNT(DISTINCT) Validation
- Orphan Record Detection

The validation was performed across all related tables including:

- Customers ↔ Orders
- Orders ↔ Order Items
- Orders ↔ Payments
- Orders ↔ Reviews
- Products ↔ Order Items

---

## SQL Techniques Used

The following SQL operations were used:

- LEFT JOIN
- COUNT()
- COUNT(DISTINCT)
- IS NULL
- GROUP BY

These queries help identify missing relationships and verify database consistency.

---

## Validation Result

After executing all integrity checks:

- No orphan customer records were found.
- No orphan order records were found.
- No orphan payment records were found.
- No orphan review records were found.
- All foreign key relationships were successfully maintained.

The imported database satisfies referential integrity requirements.

---

### Files Used

```
sql/06_integrity_checks.sql
```

---

### Screenshot

> Add:

- Referential Integrity Query
- Orphan Record Validation Output
- COUNT(DISTINCT) Results

---

# ✅ Task 6 – CSV Export

## Objective

The cleaned relational dataset generated through SQL JOIN operations was exported into a CSV file for further processing using Python.

Exporting SQL results allows analytical workflows to continue outside the database environment.

---

## Implementation

The export process was automated using Python with SQLAlchemy and PyMySQL.

The script performs the following steps:

- Connects to the MySQL database.
- Executes the INNER JOIN query.
- Loads the result into a Pandas DataFrame.
- Automatically creates the output directory.
- Exports the dataset as a CSV file.

---

## Generated Output

```
output/reports/orders_customers_join.csv
```

---

## Export Summary

| Metric | Value |
|---------|--------|
| Rows Exported | 99,441 |
| Columns Exported | 6 |
| Output Format | CSV |

---

## Advantages

- Portable dataset
- Ready for Python analysis
- Supports reproducible workflows
- Used for cleaning and statistical analysis

---

### Files Used

```
python/export_csv.py
```

---

### Screenshot

> Add:

- Terminal Output of export_csv.py
- Generated CSV File

---

# ✅ Task 7 – Data Cleaning

## Objective

Before performing statistical analysis, the exported dataset was cleaned to improve data quality and ensure consistency.

The cleaning process was implemented using **Pandas**.

---

## Data Cleaning Steps

### 1. Missing Value Analysis

Each column was analyzed to identify missing values.

Result:

- No missing values were found in the exported dataset.

---

### 2. Missing Value Treatment

Since no missing values existed, no imputation was required.

The script is capable of handling missing values automatically using suitable replacement strategies if required for future datasets.

---

### 3. Duplicate Detection

The dataset was examined for duplicate rows.

| Before Cleaning | After Cleaning |
|-----------------|---------------|
| 99,441 | 99,441 |

Duplicate Records Removed:

```
0
```

---

### 4. Clean Dataset Generation

The cleaned dataset was exported for downstream analysis.

Generated file:

```
data/cleaned/cleaned_orders.csv
```

---

### Cleaning Report

The script automatically generates a detailed report summarizing:

- Missing Values
- Duplicate Analysis
- Cleaning Summary

Generated report:

```
output/reports/data_cleaning_report.txt
```

---

### Learning Outcome

Data cleaning improves data quality by ensuring consistency, completeness, and reliability before statistical analysis.

---

### Files Used

```
python/data_cleaning.py
```

---

### Screenshot

> Add:

- Terminal Output
- Cleaned Dataset
- Data Cleaning Report

---

# ✅ Task 8 – Outlier Audit

## Objective

The objective of this task was to identify extreme observations in continuous numerical variables using statistical techniques.

Outlier detection helps identify unusual values that may influence analytical results or machine learning models.

---

## Numerical Columns Analysed

The following continuous variables were selected:

- price
- freight_value

These columns represent continuous business measurements and are suitable for statistical outlier detection.

---

## Method 1 — Interquartile Range (IQR)

The IQR method detects observations outside the range:

```
Q1 − 1.5 × IQR

Q3 + 1.5 × IQR
```

### Results

| Column | Outliers |
|---------|----------|
| price | 8,427 |
| freight_value | 12,134 |

---

## Method 2 — Z-Score

The Z-Score method measures how many standard deviations each observation lies from the mean.

Observations with an absolute Z-score greater than **3** were considered outliers.

### Results

| Column | Outliers |
|---------|----------|
| price | 1,966 |
| freight_value | 2,041 |

---

## Comparison

The **IQR method** detected a larger number of outliers because it is more robust for skewed business data and is less sensitive to extreme values.

The **Z-Score method** detected fewer outliers because it assumes the underlying data follows an approximately normal distribution.

Both techniques consistently identified **price** and **freight_value** as the primary variables containing extreme observations.

---

## Generated Report

```
output/reports/outlier_analysis_report.txt
```

---

### Files Used

```
python/outlier_analysis.py
```

---

### Screenshot

> Add:

- Terminal Output
- Outlier Analysis Report

---

# 📊 Additional Analysis (Bonus)

Although not explicitly required in the assignment, automated visualizations were generated to support exploratory data analysis.

The visualization script creates business insights directly from the exported dataset.

---

## Generated Charts

The following charts are automatically produced:

- Monthly Orders Trend
- Orders by Year
- Orders by State
- Order Status Distribution
- Top 10 Cities by Orders
- Top States Distribution (Pie Chart)

All figures are automatically saved inside:

```
images/plots/
```

---

## Generated Visualization Report

```
output/reports/visualization_report.txt
```

---

### Files Used

```
python/generate_visualizations.py
```

---

# 📂 Generated Output Files

The project automatically generates the following files during execution.

## Data Files

```
data/cleaned/
└── cleaned_orders.csv
```

## Reports

```
output/reports/
├── orders_customers_join.csv
├── data_cleaning_report.txt
├── outlier_analysis_report.txt
└── visualization_report.txt
```

## Visualizations

```
images/plots/
├── monthly_orders.png
├── orders_by_year.png
├── orders_by_state.png
├── order_status_distribution.png
├── top10_cities.png
└── top_states_pie.png
```

These outputs are automatically generated by the Python scripts and can be reproduced by following the execution steps provided below.

---

# 🖼️ Project Visualizations

The project generates several visualizations to support exploratory data analysis.

## Monthly Orders Trend

![Monthly Orders](images/plots/monthly_orders.png)

---

## Orders by Year

![Orders by Year](images/plots/orders_by_year.png)

---

## Orders by State

![Orders by State](images/plots/orders_by_state.png)

---

## Order Status Distribution

![Order Status](images/plots/order_status_distribution.png)

---

## Top 10 Cities by Orders

![Top Cities](images/plots/top10_cities.png)

---

## Top States Distribution

![Top States](images/plots/top_states_pie.png)

---

# ⚙️ Installation

## Clone the Repository

```bash
git clone https://github.com/yourusername/Data-Foundations-SQL-Extraction-Cleaning-Outlier-Audit.git
```

Move into the project directory.

```bash
cd Data-Foundations-SQL-Extraction-Cleaning-Outlier-Audit
```

Install all required dependencies.

```bash
pip install -r requirements.txt
```

---

# 📦 Requirements

The project was developed using the following library versions.

```text
pandas==2.3.3
numpy==1.26.4
SQLAlchemy==2.0.51
PyMySQL==1.2.0
matplotlib==3.10.6
scipy==1.16.1
```

---

# ▶️ How to Run

## Step 1 — Create Database

Execute:

```
database/01_schema.sql
```

This creates the relational database along with all required tables and constraints.

---

## Step 2 — Import Dataset

Before executing the import script, update the dataset location inside:

```
database/02_import_data.sql
```

Run:

```
database/02_import_data.sql
```

This imports the six original Olist datasets into the database.

---

## Step 3 — Execute SQL Queries

Run the SQL scripts in the following order:

```
sql/03_basic_queries.sql

sql/04_groupby_having.sql

sql/05_joins.sql

sql/06_integrity_checks.sql
```

---

## Step 4 — Export SQL Data

```bash
python python/export_csv.py
```

Exports the JOIN result as:

```
orders_customers_join.csv
```

---

## Step 5 — Clean the Dataset

```bash
python python/data_cleaning.py
```

Generates:

- cleaned_orders.csv
- data_cleaning_report.txt

---

## Step 6 — Perform Outlier Analysis

```bash
python python/outlier_analysis.py
```

Generates:

- outlier_analysis_report.txt

---

## Step 7 — Generate Visualizations

```bash
python python/generate_visualizations.py
```

Generates:

- Monthly Orders
- Orders by Year
- Orders by State
- Order Status Distribution
- Top 10 Cities
- Top States Pie Chart

---

# 📊 Project Results

The project was successfully completed with the following outcomes:

- Designed and implemented a normalized relational database using MySQL.
- Imported all six Olist datasets while preserving referential integrity.
- Executed SQL queries for filtering, aggregation, and business analysis.
- Validated parent-child relationships and verified database consistency.
- Exported relational data into CSV format using Python.
- Performed missing value analysis and duplicate detection using Pandas.
- Generated a cleaned dataset suitable for downstream analytics.
- Detected statistical outliers using both IQR and Z-Score methods.
- Automatically generated analytical reports for each processing stage.
- Produced reproducible visualizations directly from Python code.

---

# 🔍 Key Findings

- Successfully imported over **540,000 records** across six relational tables.
- No missing values were found in the exported analytical dataset.
- No duplicate rows were detected after cleaning.
- The **IQR method** detected more outliers than the **Z-Score method**, indicating that the numerical data is not perfectly normally distributed.
- Referential integrity validation confirmed that there were no orphan records between related tables.
- The automated workflow ensures that all reports and visualizations can be regenerated directly from the source data.

---

# 🚀 Future Improvements

Possible extensions of this project include:

- Automating the ETL pipeline.
- Building interactive dashboards using Power BI or Tableau.
- Integrating real-time data ingestion.
- Performing advanced statistical analysis.
- Developing predictive machine learning models.
- Creating automated data quality monitoring pipelines.
- Extending the project into a complete business intelligence solution.

---

# 📜 License

This project was developed for educational purposes as part of the **Data Analytics with Gen & Agentic AI Capstone Project** at **Masai School**.

The project may be freely used for learning and academic reference.

---

# 🙏 Acknowledgements

Special thanks to:

- Masai School
- Olist Brazilian E-Commerce Public Dataset
- MySQL
- MariaDB
- Pandas
- NumPy
- SQLAlchemy
- PyMySQL
- Matplotlib
- SciPy
- The Open Source Community

---

# 👩‍💻 Author

**Bhuvaneswari Yennapusala**

**B.Tech – Computer Engineering (Artificial Intelligence)**

**Masai School – Data Analytics with Gen & Agentic AI**

**Capstone Project – Part 1**

📅 **Year:** 2026

---

## ⭐ Repository

If you found this project useful, consider giving it a ⭐ on GitHub.

It helps others discover the project and supports open-source learning.

---
