/*
===============================================================================
Project : Data Foundations: SQL Extraction, Cleaning & Outlier Audit
Course  : Data Analytics with Gen & Agentic AI
Capstone: Part 1

File    : 06_integrity_checks.sql

Description:
Task 5
Referential Integrity Checks
===============================================================================
*/

USE smartcommerce_analytics;

-- ============================================================================
-- Check 1
-- COUNT(DISTINCT)
-- Number of unique customers who placed orders
-- ============================================================================

SELECT

    COUNT(DISTINCT c.customer_id) AS unique_customers

FROM customers c

INNER JOIN orders o

ON c.customer_id = o.customer_id;



-- ============================================================================
-- Check 2
-- Parent-Child Relationship
-- Customers having more than one order
-- ============================================================================

SELECT

    customer_id,

    COUNT(*) AS total_orders

FROM orders

GROUP BY customer_id

HAVING COUNT(*) > 1

ORDER BY total_orders DESC;



-- ============================================================================
-- Check 3
-- Orphan Check
-- Orders without matching customers
-- ============================================================================

SELECT

    o.order_id,

    o.customer_id

FROM orders o

LEFT JOIN customers c

ON o.customer_id = c.customer_id

WHERE c.customer_id IS NULL;