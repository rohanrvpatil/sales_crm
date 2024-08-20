import pandas as pd
import sqlite3

df = pd.read_excel("dummy_saas_data.xlsx")

df["Subscription Start Date"] = pd.to_datetime(
    df["Subscription Start Date"]
).dt.strftime("%Y-%m-%d")
df["Subscription End Date"] = pd.to_datetime(df["Subscription End Date"]).dt.strftime(
    "%Y-%m-%d"
)

# Connect to SQLite database
conn = sqlite3.connect("customers.db")
cursor = conn.cursor()

# Insert DataFrame records one by one.
for i, row in df.iterrows():
    cursor.execute(
        """
        INSERT INTO customers (
            customer_id, customer_name, company_name, email, phone, address, subscription_plan,
            subscription_start_date, subscription_end_date, billing_cycle, payment_status, product_usage,
            account_manager, customer_segment, customer_feedback, revenue
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """,
        tuple(row),
    )

conn.commit()
conn.close()
