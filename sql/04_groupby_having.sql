/*
===============================================================================
Project : Data Foundations: SQL Extraction, Cleaning & Outlier Audit
Course  : Data Analytics with Gen & Agentic AI
Capstone: Part 1

File    : 04_groupby_having.sql

Description:
Task 3
GROUP BY + HAVING Query
===============================================================================
*/

USE smartcommerce_analytics;

SELECT

    p.payment_type,

    COUNT(*) AS total_transactions,

    SUM(p.payment_value) AS total_sales,

    AVG(p.payment_value) AS average_payment

FROM payments p

GROUP BY p.payment_type

HAVING SUM(p.payment_value) > 100000

ORDER BY total_sales DESC;