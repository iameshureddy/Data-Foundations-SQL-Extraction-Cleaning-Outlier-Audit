SELECT

    c.customer_id,

    c.customer_city,

    c.customer_state,

    o.order_id,

    o.order_status

FROM customers c

LEFT JOIN orders o

ON c.customer_id = o.customer_id;