/*
Project : Data Foundations: SQL Extraction, Cleaning & Outlier Audit
Course  : Data Analytics with Gen & Agentic AI
Capstone: Part 1

File    : 06_integrity_checks.sql

Task    : Task 5 - Referential Integrity Validation

Objective:
Validate the relationship between the customers and orders tables
and check for duplicate parent-child relationships and orphan records.

Tables Used:
1. customers - Parent Table
2. orders    - Child Table

Relationship:
customers.customer_id -> orders.customer_id

The relationship is validated using:
1. COUNT(DISTINCT ...) check
2. GROUP BY + COUNT(*) cardinality check
3. Orphan-record check

Author  : Bhuvaneswari Yennapusala
*/

USE smartcommerce_analytics;


-- ============================================================================
-- CHECK 1: DISTINCT PARENT KEYS WITH MATCHING CHILD RECORDS
-- ============================================================================
-- Purpose:
-- Count the number of unique customers that have at least one matching
-- order.
--
-- Why?
-- This confirms that customer IDs from the parent table are successfully
-- linked to order records.
--
-- Important:
-- COUNT(DISTINCT ...) alone cannot determine whether the relationship is
-- 1:1 or 1:M. Therefore, Check 2 is also required.
-- ============================================================================

SELECT
    COUNT(DISTINCT c.customer_id) AS unique_customers_with_orders
FROM customers AS c
INNER JOIN orders AS o
    ON c.customer_id = o.customer_id;


-- ============================================================================
-- CHECK 2: CARDINALITY / 1:1 OR 1:M VALIDATION
-- ============================================================================
-- Purpose:
-- Count the number of orders associated with each customer.
--
-- Why?
-- This determines whether any customer has more than one order.
--
-- Interpretation:
-- If rows are returned:
--     At least one customer has multiple orders -> 1:M relationship exists.
--
-- If zero rows are returned:
--     No customer has more than one order -> relationship is 1:1
--     for customer_id in this schema.
-- ============================================================================

SELECT
    o.customer_id,
    COUNT(o.order_id) AS total_orders
FROM orders AS o
GROUP BY o.customer_id
HAVING COUNT(o.order_id) > 1
ORDER BY total_orders DESC;


-- ============================================================================
-- CHECK 3: ORPHAN ORDER CHECK
-- ============================================================================
-- Purpose:
-- Find orders whose customer_id does not exist in the customers table.
--
-- Why?
-- Every order should reference an existing customer.
--
-- Interpretation:
-- If zero rows are returned:
--     No orphan orders exist and referential integrity is maintained.
--
-- If rows are returned:
--     Those orders have no matching customer record.
-- ============================================================================

SELECT
    o.order_id,
    o.customer_id
FROM orders AS o
LEFT JOIN customers AS c
    ON o.customer_id = c.customer_id
WHERE c.customer_id IS NULL;