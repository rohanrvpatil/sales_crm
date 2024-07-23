/*
sqlite3 customers.db < schema.sql

The above code is run to create a customers.db SQL database file using the code in schema.sql
*/

-- The below code defines schema for customer.db database file 

CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT,
    address TEXT,
    notes TEXT
);
