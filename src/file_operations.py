import sqlite3
import time
from src.customer import Customer
import pandas as pd

DATABASE = "./database/customers.db"


# decorator function
def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = round(end_time - start_time, 4)
        print(f"Execution time for {func.__name__}: {execution_time} seconds")
        return result

    return wrapper


# context manager
class DatabaseConnection:
    def __enter__(self):
        self.conn = sqlite3.connect(DATABASE)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_value, traceback):
        self.conn.commit()
        self.conn.close()
        return False


def save_customers(customers):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # Clear the existing data if needed
    cursor.execute("DELETE FROM customers")

    # Insert or replace data from the DataFrame
    for _, row in customers.iterrows():
        subscription_start_date = (
            row["subscription_start_date"].strftime("%Y-%m-%d")
            if pd.notna(row["subscription_start_date"])
            else None
        )
        subscription_end_date = (
            row["subscription_end_date"].strftime("%Y-%m-%d")
            if pd.notna(row["subscription_end_date"])
            else None
        )

        cursor.execute(
            """
            INSERT OR REPLACE INTO customers (
                customer_id, customer_name, company_name, email, phone, address,
                subscription_plan, subscription_start_date, subscription_end_date,
                billing_cycle, payment_status, product_usage, account_manager,
                customer_segment, customer_feedback, revenue
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
            (
                row["customer_id"],
                row["customer_name"],
                row["company_name"],
                row["email"],
                row["phone"],
                row["address"],
                row["subscription_plan"],
                row["subscription_start_date"],
                row["subscription_end_date"],
                row["billing_cycle"],
                row["payment_status"],
                row["product_usage"],
                row["account_manager"],
                row["customer_segment"],
                row["customer_feedback"],
                row["revenue"],
            ),
        )

    conn.commit()
    conn.close()


# decorator
@measure_time
def load_customers():
    # generator
    def customer_generator():
        with DatabaseConnection() as cursor:
            cursor.execute(
                """
                SELECT customer_id, customer_name, company_name, email, phone, address,
                       subscription_plan, subscription_start_date, subscription_end_date,
                       billing_cycle, payment_status, product_usage, account_manager,
                       customer_segment, customer_feedback, revenue
                FROM customers
            """
            )
            rows = cursor.fetchall()
            for row in rows:
                yield {
                    "customer_id": row[0],
                    "customer_name": row[1],
                    "company_name": row[2],
                    "email": row[3],
                    "phone": row[4],
                    "address": row[5],
                    "subscription_plan": row[6],
                    "subscription_start_date": row[7],
                    "subscription_end_date": row[8],
                    "billing_cycle": row[9],
                    "payment_status": row[10],
                    "product_usage": row[11],
                    "account_manager": row[12],
                    "customer_segment": row[13],
                    "customer_feedback": row[14],
                    "revenue": row[15],
                }

    customers = list(customer_generator())
    df = pd.DataFrame(customers)

    df["subscription_start_date"] = pd.to_datetime(df["subscription_start_date"])
    df["subscription_end_date"] = pd.to_datetime(df["subscription_end_date"])

    return df


def delete_customer(customer_name):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(
        """
        DELETE FROM customers WHERE customer_name = ?
    """,
        (customer_name,),
    )
    conn.commit()
    conn.close()
