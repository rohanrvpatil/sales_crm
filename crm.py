from customer import Customer
import sqlite3


class CRM:
    def __init__(self, db_name="customers.db"):
        #these are different parts of the class state

        #saving the database name for future use
        self.db_name = db_name

        self.customers = []
        self.next_id = 1

    
    
    def add_customer(self, customer):
        customer.customer_id = self.next_id
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()

        c.execute('''
        INSERT INTO customers (customer_id, name, email, phone, address, notes)
        VALUES (?, ?, ?, ?, ?, ?)
        ''', (customer.customer_id, customer.name, customer.email, customer.phone, customer.address, customer.notes))
        conn.commit()

        conn.close()
        self.next_id += 1
        print("Customer added successfully.")
   
    

    def view_customers(self):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute('SELECT * FROM customers')
        customers = c.fetchall()
        conn.close()
        if not customers:
            print("No customers found.")
        else:
            for customer in customers:
                print(f"Customer ID: {customer[0]}, Name: {customer[1]}, Email: {customer[2]}, "
                      f"Phone: {customer[3]}, Address: {customer[4]}, Notes: {customer[5]}")

    #search_customer function before using lambda function
    """
    def search_customer(self, search_name):
        found_customers = [customer for customer in self.customers if customer.name.lower() == search_name.lower()]
        if not found_customers:
            print("No customer found with that name.")
        else:
            for customer in found_customers:
                print(f"Found Customer: {customer}")
    """

    #search_customer function after using lambda function
    def search_customer(self, search_name):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute('SELECT * FROM customers WHERE LOWER(name) = ?', (search_name.lower(),))
        customers = c.fetchall()
        conn.close()
        if not customers:
            print("No customer found with that name.")
        else:
            for customer in customers:
                print(f"Found Customer: ID: {customer[0]}, Name: {customer[1]}, Email: {customer[2]}, "
                      f"Phone: {customer[3]}, Address: {customer[4]}, Notes: {customer[5]}")


    def delete_customer(self, delete_name):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute('DELETE FROM customers WHERE LOWER(name) = ?', (delete_name.lower(),))
        conn.commit()
        conn.close()
        print("Customer deleted successfully.")