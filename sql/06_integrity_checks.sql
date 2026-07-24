/*
===============================================================================
Project : Data Foundations: SQL Extraction, Cleaning & Outlier Audit
Course  : Data Analytics with Gen & Agentic AI
Capstone: Part 1

File    : 06_integrity_checks.sql

Task    : Task 5 - Referential Integrity Validation

Objective:
Validate the relationships between the 'customers' and 'orders' tables to
ensure that the database maintains referential integrity.

Tables Used:
1. customers (Parent Table)
2. orders    (Child Table)

Relationship:
One Customer → Many Orders (1:M)

Foreign Key:
orders.customer_id → customers.customer_id
===============================================================================
*/

USE smartcommerce_analytics;

-- ============================================================================
-- CHECK 1: Verify Unique Customers with Orders
-- ============================================================================
-- Objective:
-- Count the number of distinct customers who have placed at least one order.
--
-- Why?
-- Ensures that customer records are correctly linked with the orders table.
-- ============================================================================

SELECT
    COUNT(DISTINCT c.customer_id) AS unique_customers
FROM customers AS c
INNER JOIN orders AS o
       ON c.customer_id = o.customer_id;



-- ============================================================================
-- CHECK 2: Validate Parent–Child Relationship
-- ============================================================================
-- Objective:
-- Identify customers who have placed more than one order.
--
-- Why?
-- Demonstrates the One-to-Many relationship where one customer can have
-- multiple orders.
-- ============================================================================

SELECT
    o.customer_id,
    COUNT(o.order_id) AS total_orders
FROM orders AS o
GROUP BY o.customer_id
HAVING COUNT(o.order_id) > 1
ORDER BY total_orders DESC;



-- ============================================================================
-- CHECK 3: Detect Orphan Records
-- ============================================================================
-- Objective:
-- Find orders that do not have a corresponding customer record.
--
-- Why?
-- Every order should reference an existing customer.
-- If this query returns zero rows, referential integrity is successfully
-- maintained.
-- ============================================================================

SELECT
    o.order_id,
    o.customer_id
FROM orders AS o
LEFT JOIN customers AS c
       ON o.customer_id = c.customer_id
WHERE c.customer_id IS NULL;



-- ============================================================================
-- EXPECTED RESULTS
-- ============================================================================
-- Check 1:
-- Returns the total number of unique customers who have placed orders.
--
-- Check 2:
-- Lists customers with multiple orders, confirming the One-to-Many
-- relationship.
--
-- Check 3:
-- Ideally returns zero rows, indicating there are no orphan orders and
-- referential integrity is maintained.
-- ============================================================================