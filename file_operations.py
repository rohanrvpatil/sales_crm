import sqlite3
import time
from customer import Customer

DATABASE = 'customers.db'

#decorator function
def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = round(end_time - start_time, 4)
        print(f"Execution time for {func.__name__}: {execution_time} seconds")
        return result
    return wrapper

#context manager
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
    for customer in customers:
        cursor.execute('''
            INSERT OR REPLACE INTO customers (
                customer_id, customer_name, company_name, email, phone, address,
                subscription_plan, subscription_start_date, subscription_end_date,
                billing_cycle, payment_status, product_usage, account_manager,
                customer_segment, customer_feedback
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            customer.customer_id, customer.customer_name, customer.company_name, customer.email,
            customer.phone, customer.address, customer.subscription_plan, customer.subscription_start_date,
            customer.subscription_end_date, customer.billing_cycle, customer.payment_status,
            customer.product_usage, customer.account_manager, customer.customer_segment,
            customer.customer_feedback
        ))
    
    conn.commit()
    conn.close()

#decorator
@measure_time
def load_customers():
    #generator
    def customer_generator():
        with DatabaseConnection() as cursor:
            cursor.execute('''
                SELECT customer_id, customer_name, company_name, email, phone, address,
                       subscription_plan, subscription_start_date, subscription_end_date,
                       billing_cycle, payment_status, product_usage, account_manager,
                       customer_segment, customer_feedback
                FROM customers
            ''')
            rows = cursor.fetchall()
            for row in rows:
                yield Customer(
                    customer_id=row[0], customer_name=row[1], company_name=row[2], email=row[3],
                    phone=row[4], address=row[5], subscription_plan=row[6], 
                    subscription_start_date=row[7], subscription_end_date=row[8],
                    billing_cycle=row[9], payment_status=row[10], product_usage=row[11],
                    account_manager=row[12], customer_segment=row[13], customer_feedback=row[14]
                )

    return list(customer_generator())


def delete_customer(customer_name):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        DELETE FROM customers WHERE customer_name = ?
    ''', (customer_name,))
    conn.commit()
    conn.close()