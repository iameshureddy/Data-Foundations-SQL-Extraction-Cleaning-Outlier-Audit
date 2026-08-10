/*
Project : Data Foundations: SQL Extraction, Cleaning & Outlier Audit
Course  : Data Analytics with Gen & Agentic AI
Capstone: Part 1

File    : 04_groupby_having.sql

Description:
This file demonstrates GROUP BY, HAVING, and aggregate functions
using the payments table.

Database : smartcommerce_analytics
Dataset  : Olist Brazilian E-Commerce Dataset

Task    : Task 3 - GROUP BY + HAVING

Author  : Bhuvaneswari Yennapusala
*/

USE smartcommerce_analytics;

-- ============================================================================
-- Task 3: GROUP BY + HAVING
-- ============================================================================
-- Objective:
-- Group payment transactions by payment type and calculate:
--   1. Total number of transactions
--   2. Total sales amount
--   3. Average payment value
--
-- HAVING is used to keep only payment types whose total sales
-- are greater than 100,000.
-- ============================================================================

SELECT
    p.payment_type,
    COUNT(*) AS total_transactions,
    SUM(p.payment_value) AS total_sales,
    AVG(p.payment_value) AS average_payment
FROM payments AS p
GROUP BY p.payment_type
HAVING SUM(p.payment_value) > 100000
ORDER BY total_sales DESC;