/*
===============================================================================
Project : Data Foundations: SQL Extraction, Cleaning & Outlier Audit
Course  : Data Analytics with Gen & Agentic AI
Capstone: Part 1

File    : 03_basic_queries.sql

Description:
This file contains the six SQL query types required in Task 2.

Database : smartcommerce_analytics
Dataset  : Olist Brazilian E-Commerce Dataset

Author   : Bhuvaneswari Yennapusala
===============================================================================
*/

USE smartcommerce_analytics;

-- ============================================================================
-- Query 1
-- WHERE ... IN
-- Find delivered or shipped orders
-- ============================================================================

SELECT
    order_id,
    customer_id,
    order_status
FROM orders
WHERE order_status IN ('delivered','shipped');



-- ============================================================================
-- Query 2: WHERE ... NOT IN
-- Find orders whose status is not cancelled or unavailable
-- Uses the SAME column as Query 1: order_status
-- ============================================================================

SELECT
    order_id,
    customer_id,
    order_status
FROM orders
WHERE order_status NOT IN
(
    'cancelled',
    'unavailable'
);

-- ============================================================================
-- Query 3
-- BETWEEN
-- Orders purchased during 2018
-- ============================================================================

SELECT
    order_id,
    customer_id,
    order_purchase_timestamp
FROM orders
WHERE order_purchase_timestamp
BETWEEN '2018-01-01 00:00:00'
AND '2018-12-31 23:59:59';


-- ============================================================================
-- Query 4
-- ORDER BY
-- Sort using two columns
-- (price DESC, freight ASC)
-- ============================================================================

SELECT
    order_id,
    product_id,
    price,
    freight_value
FROM order_items
ORDER BY
price DESC,
freight_value ASC;



-- ============================================================================
-- Query 5
-- NOT EXISTS
-- Customers who never placed any order
-- ============================================================================

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



-- ============================================================================
-- Query 6
-- LIKE
-- Customers living in cities containing 'paulo'
-- ============================================================================

SELECT
    customer_id,
    customer_city,
    customer_state
FROM customers
WHERE customer_city
LIKE '%paulo%';