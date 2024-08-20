/*
sqlite3 customers.db < schema.sql

The above code is run to create a customers.db SQL database file using the code in schema.sql
*/

-- The below code defines schema for customer.db database file 

CREATE TABLE customers (
    customer_id TEXT PRIMARY KEY,
    customer_name TEXT,
    company_name TEXT,
    email TEXT,
    phone TEXT,
    address TEXT,
    subscription_plan TEXT,
    subscription_start_date DATE,
    subscription_end_date DATE,
    billing_cycle TEXT,
    payment_status TEXT,
    product_usage INTEGER,
    account_manager TEXT,
    customer_segment TEXT,
    customer_feedback TEXT,
    revenue INTEGER
);

