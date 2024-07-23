import streamlit as st
import sqlite3
from customer import Customer
from file_operations import save_customers, load_customers

def main():
    st.title("Customer Relationship Management")

    menu = ["Add Customer", "View Customers", "Search Customer", "Delete Customer"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Add Customer":
        with st.form(key='add_customer_form'):
            name = st.text_input("Name")
            email = st.text_input("Email")
            phone = st.text_input("Phone")
            address = st.text_input("Address")
            notes = st.text_area("Notes")
            submit_button = st.form_submit_button(label='Add Customer')

            if submit_button:
                customer = Customer(None, name, email, phone, address, notes)
                customers = load_customers()
                customer.customer_id = len(customers) + 1
                customers.append(customer)
                save_customers(customers)
                st.success("Customer added successfully!")

    elif choice == "View Customers":
        customers = load_customers()
        if not customers:
            st.write("No customers found.")
        else:
            for customer in customers:
                st.write(customer)

    elif choice == "Search Customer":
        search_name = st.text_input("Enter customer name:")
        if st.button("Search"):
            customers = load_customers()
            found_customers = [customer for customer in customers if search_name.lower() in customer.name.lower()]
            if not found_customers:
                st.write("No customer found.")
            else:
                for customer in found_customers:
                    st.write(customer)

    elif choice == "Delete Customer":
        delete_name = st.text_input("Enter customer name to delete:")
        if st.button("Delete"):
            customers = load_customers()
            customers = [customer for customer in customers if customer.name.lower() != delete_name.lower()]
            save_customers(customers)
            st.success("Customer deleted successfully!")

if __name__ == "__main__":
    main()
