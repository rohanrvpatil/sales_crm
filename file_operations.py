import sqlite3
from customer import Customer

DATABASE = 'customers.db'

def save_customers(customers):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    
    # Insert or replace customer data
    for customer in customers:
        cursor.execute('''
            INSERT OR REPLACE INTO customers (customer_id, name, email, phone, address, notes)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (customer.customer_id, customer.name, customer.email, customer.phone, customer.address, customer.notes))
    
    conn.commit()
    conn.close()

def load_customers():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM customers')
    rows = cursor.fetchall()
    
    conn.close()
    
    return [Customer(customer_id=row[0], name=row[1], email=row[2], phone=row[3], address=row[4], notes=row[5]) for row in rows]
