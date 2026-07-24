-- ============================================================================
-- FILE: 05_joins.sql
-- PROJECT: Data Foundations – SQL Extraction, Cleaning & Outlier Audit
-- TASK 4: Demonstrating INNER JOIN and LEFT JOIN
--
-- Purpose:
-- This file demonstrates two different SQL JOIN operations between the
-- 'customers' and 'orders' tables.
--
-- Tables Used:
--   1. customers
--   2. orders
--
-- Relationship:
--   One Customer --> Many Orders (1:M)
--
-- Foreign Key:
--   orders.customer_id references customers.customer_id
--
-- Why this task?
--   The rubric requires demonstrating both INNER JOIN and LEFT JOIN,
--   along with explaining why each join is used.
-- ============================================================================



-- ============================================================================
-- TASK 4A : INNER JOIN
-- ============================================================================
--
-- Purpose:
-- Retrieve only customers who have placed at least one order.
--
-- Why INNER JOIN?
-- INNER JOIN returns only those rows where a matching customer_id exists
-- in both the customers and orders tables.
--
-- Use Case:
-- Useful for analysing completed customer transactions because only
-- customers with existing orders are included.
--
-- Expected Output:
-- Customer information together with corresponding order details.
-- Customers without orders are excluded.
-- ============================================================================

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



-- ============================================================================
-- TASK 4B : LEFT JOIN
-- ============================================================================
--
-- Purpose:
-- Retrieve every customer, regardless of whether they have placed an order.
--
-- Why LEFT JOIN?
-- The customers table is placed on the LEFT because we want to retain
-- every customer record in the final result.
--
-- If a customer has not placed any order,
-- the order columns will contain NULL values.
--
-- Use Case:
-- Helps identify customers who have never placed an order and supports
-- customer retention analysis.
--
-- Expected Output:
-- All customers appear in the result.
-- Order details appear only where matching records exist.
-- ============================================================================

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