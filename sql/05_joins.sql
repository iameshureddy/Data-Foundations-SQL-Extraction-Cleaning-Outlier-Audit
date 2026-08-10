/*
Project : Data Foundations: SQL Extraction, Cleaning & Outlier Audit
Course  : Data Analytics with Gen & Agentic AI
Capstone: Part 1

File    : 05_joins.sql

Description:
This file demonstrates INNER JOIN and LEFT JOIN operations
between the customers and orders tables.

Database : smartcommerce_analytics
Dataset  : Olist Brazilian E-Commerce Dataset

Task    : Task 4 - JOIN Operations

Relationship:
One Customer --> Many Orders (1:M)

Foreign Key:
orders.customer_id references customers.customer_id

Author  : Bhuvaneswari Yennapusala
*/

USE smartcommerce_analytics;


-- ============================================================================
-- TASK 4A: INNER JOIN
-- ============================================================================
-- Purpose:
-- Retrieve customers who have at least one matching order.
--
-- Why INNER JOIN?
-- INNER JOIN returns only records where customer_id exists in both
-- customers and orders.
--
-- Result:
-- Customers without matching orders are excluded.
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
-- TASK 4B: LEFT JOIN
-- ============================================================================
-- Purpose:
-- Retrieve every customer, including customers who have no matching order.
--
-- Why LEFT JOIN?
-- The customers table is placed on the LEFT side because the objective
-- is to retain every customer record.
--
-- If a customer has no matching order, the order-related columns
-- will contain NULL values.
--
-- Result:
-- All customers are retained, while matching order information is
-- included when available.
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