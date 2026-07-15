/*
===============================================================================
 Project Title : Data Foundations: SQL Extraction, Cleaning & Outlier Audit
 Course        : Data Analytics with Gen & Agentic AI
 Capstone      : Part 1

 File          : 02_import_data.sql
 Database      : smartcommerce_analytics
 Dataset       : Olist Brazilian E-Commerce Public Dataset

 Author        : Bhuvaneswari Yennapusala
 Date          : 15-07-2026

 Description:
 This script imports the original Olist Brazilian E-Commerce CSV datasets
 into the smartcommerce_analytics database using LOAD DATA LOCAL INFILE.

 Features
 --------
 ✓ Imports all six datasets
 ✓ Converts date/time columns to DATETIME
 ✓ Preserves referential integrity
 ✓ Validates each import using COUNT(*)
 ✓ Displays a final import summary

------------------------------------------------------------------------------
 Dataset Location
------------------------------------------------------------------------------

Place all original Kaggle CSV files inside:

data/raw/

Replace <PATH_TO_DATASET> with the absolute path to your local
data/raw folder.

Example (Windows)

C:/Users/YourName/Documents/Data-Foundations-SQL-Extraction-Cleaning-Outlier-Audit/data/raw

Example (Linux/macOS)

/home/username/Data-Foundations-SQL-Extraction-Cleaning-Outlier-Audit/data/raw

===============================================================================
*/

USE smartcommerce_analytics;

-- ============================================================================
-- 1. IMPORT CUSTOMERS
-- ============================================================================

LOAD DATA LOCAL INFILE
'<PATH_TO_DATASET>/olist_customers_dataset.csv'
INTO TABLE customers
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(
    customer_id,
    customer_unique_id,
    customer_zip_code_prefix,
    customer_city,
    customer_state
);

SELECT COUNT(*) AS total_customers
FROM customers;

-- ============================================================================
-- 2. IMPORT PRODUCTS
-- ============================================================================

LOAD DATA LOCAL INFILE
'<PATH_TO_DATASET>/olist_products_dataset.csv'
INTO TABLE products
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(
    product_id,
    product_category_name,
    product_name_length,
    product_description_length,
    product_photos_qty,
    product_weight_g,
    product_length_cm,
    product_height_cm,
    product_width_cm
);

SELECT COUNT(*) AS total_products
FROM products;

-- ============================================================================
-- 3. IMPORT ORDERS
-- ============================================================================

LOAD DATA LOCAL INFILE
'<PATH_TO_DATASET>/olist_orders_dataset.csv'
INTO TABLE orders
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(
    order_id,
    customer_id,
    order_status,
    @purchase,
    @approved,
    @carrier,
    @customer,
    @estimated
)
SET

order_purchase_timestamp =
CASE
WHEN @purchase='' THEN NULL
ELSE STR_TO_DATE(@purchase,'%Y-%m-%d %H:%i:%s')
END,

order_approved_at =
CASE
WHEN @approved='' THEN NULL
ELSE STR_TO_DATE(@approved,'%Y-%m-%d %H:%i:%s')
END,

order_delivered_carrier_date =
CASE
WHEN @carrier='' THEN NULL
ELSE STR_TO_DATE(@carrier,'%Y-%m-%d %H:%i:%s')
END,

order_delivered_customer_date =
CASE
WHEN @customer='' THEN NULL
ELSE STR_TO_DATE(@customer,'%Y-%m-%d %H:%i:%s')
END,

order_estimated_delivery_date =
CASE
WHEN @estimated='' THEN NULL
ELSE STR_TO_DATE(@estimated,'%Y-%m-%d %H:%i:%s')
END;

SELECT COUNT(*) AS total_orders
FROM orders;

-- ============================================================================
-- 4. IMPORT ORDER ITEMS
-- ============================================================================

LOAD DATA LOCAL INFILE
'<PATH_TO_DATASET>/olist_order_items_dataset.csv'
INTO TABLE order_items
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(
    order_id,
    order_item_id,
    product_id,
    seller_id,
    @shipping_limit_date,
    price,
    freight_value
)
SET

shipping_limit_date =
CASE
WHEN @shipping_limit_date='' THEN NULL
ELSE STR_TO_DATE(@shipping_limit_date,'%Y-%m-%d %H:%i:%s')
END;

SELECT COUNT(*) AS total_order_items
FROM order_items;

-- ============================================================================
-- 5. IMPORT PAYMENTS
-- ============================================================================

LOAD DATA LOCAL INFILE
'<PATH_TO_DATASET>/olist_order_payments_dataset.csv'
INTO TABLE payments
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(
    order_id,
    payment_sequential,
    payment_type,
    payment_installments,
    payment_value
);

SELECT COUNT(*) AS total_payments
FROM payments;

-- ============================================================================
-- 6. IMPORT REVIEWS
-- ============================================================================

LOAD DATA LOCAL INFILE
'<PATH_TO_DATASET>/olist_order_reviews_dataset.csv'
INTO TABLE reviews
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(
    review_id,
    order_id,
    review_score,
    review_comment_title,
    review_comment_message,
    @creation_date,
    @answer_timestamp
)
SET

review_creation_date =
CASE
WHEN @creation_date='' THEN NULL
ELSE STR_TO_DATE(@creation_date,'%Y-%m-%d %H:%i:%s')
END,

review_answer_timestamp =
CASE
WHEN @answer_timestamp='' THEN NULL
ELSE STR_TO_DATE(@answer_timestamp,'%Y-%m-%d %H:%i:%s')
END;

SELECT COUNT(*) AS total_reviews
FROM reviews;

-- ============================================================================
-- IMPORT SUMMARY
-- ============================================================================

SELECT 'Customers' AS Table_Name, COUNT(*) AS Total_Records
FROM customers

UNION ALL

SELECT 'Products', COUNT(*)
FROM products

UNION ALL

SELECT 'Orders', COUNT(*)
FROM orders

UNION ALL

SELECT 'Order Items', COUNT(*)
FROM order_items

UNION ALL

SELECT 'Payments', COUNT(*)
FROM payments

UNION ALL

SELECT 'Reviews', COUNT(*)
FROM reviews;

-- ============================================================================
-- EXPECTED RECORD COUNTS
-- ============================================================================

/*

Customers      : 99,441
Products       : 32,951
Orders         : 99,441
Order Items    : 112,650
Payments       : 103,886
Reviews         : 99,224

If your imported row counts match these values, the import
completed successfully and the database is ready for analysis.

*/

-- ============================================================================
-- END OF FILE
-- ============================================================================