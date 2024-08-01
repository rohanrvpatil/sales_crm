import pandas as pd
import sqlite3

# Load data from Excel file
df = pd.read_excel('dummy_saas_data.xlsx')

df['Subscription Start Date'] = pd.to_datetime(df['Subscription Start Date']).dt.strftime('%Y-%m-%d')
df['Subscription End Date'] = pd.to_datetime(df['Subscription End Date']).dt.strftime('%Y-%m-%d')

# Connect to SQLite database (it will create the database if it doesn't exist)
conn = sqlite3.connect('customers.db')
cursor = conn.cursor()

# Create the table
cursor.execute('''
CREATE TABLE IF NOT EXISTS customers (
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
    customer_feedback TEXT
)
''')

# Insert DataFrame records one by one.
for i, row in df.iterrows():
    cursor.execute('''
        INSERT INTO customers (
            customer_id, customer_name, company_name, email, phone, address, subscription_plan,
            subscription_start_date, subscription_end_date, billing_cycle, payment_status, product_usage,
            account_manager, customer_segment, customer_feedback
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', tuple(row))

# Commit the transaction
conn.commit()

# Close the connection
conn.close()
