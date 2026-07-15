/*
===============================================================================
Project Title : Data Foundations: SQL Extraction, Cleaning & Outlier Audit
Course        : Data Analytics with Gen & Agentic AI
Capstone      : Part 1
Database      : smartcommerce_analytics
Dataset       : Olist Brazilian E-Commerce Public Dataset

Author        : Bhuvaneswari Yennapusala
Date          : 15-07-2026

Description:
This SQL script creates the relational database schema for the
Olist Brazilian E-Commerce dataset. It defines all required tables,
primary keys, foreign keys, and referential integrity constraints
needed for Part 1 of the capstone project.

Database Engine : MariaDB / MySQL
Character Set   : utf8mb4
Storage Engine  : InnoDB
===============================================================================
*/

-- ============================================================================
-- Create Database
-- ============================================================================

CREATE DATABASE IF NOT EXISTS smartcommerce_analytics
CHARACTER SET utf8mb4
COLLATE utf8mb4_general_ci;

USE smartcommerce_analytics;

-- ============================================================================
-- Remove Existing Tables (Child Tables First)
-- ============================================================================

SET FOREIGN_KEY_CHECKS = 0;

DROP TABLE IF EXISTS reviews;
DROP TABLE IF EXISTS payments;
DROP TABLE IF EXISTS order_items;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS customers;

SET FOREIGN_KEY_CHECKS = 1;

-- ============================================================================
-- TABLE : CUSTOMERS
-- Stores customer demographic information.
-- One customer can place multiple orders.
-- ============================================================================

CREATE TABLE customers (

    customer_id VARCHAR(50) NOT NULL,
    customer_unique_id VARCHAR(50) NOT NULL,
    customer_zip_code_prefix INT,
    customer_city VARCHAR(100),
    customer_state CHAR(2),

    PRIMARY KEY (customer_id)

) ENGINE=InnoDB;

-- ============================================================================
-- TABLE : PRODUCTS
-- Stores product information.
-- One product can appear in multiple order items.
-- ============================================================================

CREATE TABLE products (

    product_id VARCHAR(50) NOT NULL,
    product_category_name VARCHAR(100),
    product_name_length INT,
    product_description_length INT,
    product_photos_qty INT,
    product_weight_g INT,
    product_length_cm INT,
    product_height_cm INT,
    product_width_cm INT,

    PRIMARY KEY (product_id)

) ENGINE=InnoDB;

-- ============================================================================
-- TABLE : ORDERS
-- Stores customer orders.
-- Each order belongs to exactly one customer.
-- ============================================================================

CREATE TABLE orders (

    order_id VARCHAR(50) NOT NULL,
    customer_id VARCHAR(50) NOT NULL,

    order_status VARCHAR(30),

    order_purchase_timestamp DATETIME,

    order_approved_at DATETIME,

    order_delivered_carrier_date DATETIME,

    order_delivered_customer_date DATETIME,

    order_estimated_delivery_date DATETIME,

    PRIMARY KEY (order_id),

    CONSTRAINT fk_orders_customer
        FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT

) ENGINE=InnoDB;

-- ============================================================================
-- TABLE : ORDER_ITEMS
-- Stores products included in each order.
-- Composite Primary Key:
--     (order_id, order_item_id)
-- ============================================================================

CREATE TABLE order_items (

    order_id VARCHAR(50) NOT NULL,

    order_item_id INT NOT NULL,

    product_id VARCHAR(50) NOT NULL,

    seller_id VARCHAR(50),

    shipping_limit_date DATETIME,

    price DECIMAL(10,2),

    freight_value DECIMAL(10,2),

    PRIMARY KEY (order_id, order_item_id),

    CONSTRAINT fk_orderitems_order
        FOREIGN KEY (order_id)
        REFERENCES orders(order_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT fk_orderitems_product
        FOREIGN KEY (product_id)
        REFERENCES products(product_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT

) ENGINE=InnoDB;

-- ============================================================================
-- TABLE : PAYMENTS
-- Stores payment information for each order.
-- Composite Primary Key:
--     (order_id, payment_sequential)
-- ============================================================================

CREATE TABLE payments (

    order_id VARCHAR(50) NOT NULL,

    payment_sequential INT NOT NULL,

    payment_type VARCHAR(30),

    payment_installments INT,

    payment_value DECIMAL(10,2),

    PRIMARY KEY (order_id, payment_sequential),

    CONSTRAINT fk_payments_order
        FOREIGN KEY (order_id)
        REFERENCES orders(order_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT

) ENGINE=InnoDB;

-- ============================================================================
-- TABLE : REVIEWS
-- Stores customer review information.
-- Each review is associated with one order.
-- ============================================================================

CREATE TABLE reviews (

    review_id VARCHAR(50) NOT NULL,

    order_id VARCHAR(50) NOT NULL,

    review_score INT,

    review_comment_title TEXT,

    review_comment_message TEXT,

    review_creation_date DATETIME,

    review_answer_timestamp DATETIME,

    PRIMARY KEY (review_id),

    CONSTRAINT fk_reviews_order
        FOREIGN KEY (order_id)
        REFERENCES orders(order_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT

) ENGINE=InnoDB;

-- ============================================================================
-- RELATIONSHIP SUMMARY
--
-- customers (1) --------< orders (M)
-- orders (1) -----------< order_items (M)
-- products (1) ---------< order_items (M)
-- orders (1) -----------< payments (M)
-- orders (1) -----------< reviews (M)
--
-- Primary Keys      : 6
-- Foreign Keys      : 5
-- Composite Keys    : 2
--
-- Database Schema Successfully Created
-- ============================================================================