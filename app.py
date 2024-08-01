import streamlit as st
import pandas as pd
from customer import Customer
from file_operations import save_customers, load_customers, delete_customer

def main():
    st.title("Customer Relationship Management")

    menu = ["Add Customer", "View Customers", "Search Customer", "Delete Customer"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Add Customer":
        with st.form(key='add_customer_form'):
            customer_id = st.text_input("Customer ID")
            customer_name = st.text_input("Customer Name")
            company_name = st.text_input("Company Name")
            email = st.text_input("Email")
            phone = st.text_input("Phone")
            address = st.text_input("Address")
            subscription_plan = st.text_input("Subscription Plan")
            subscription_start_date = st.date_input("Subscription Start Date")
            subscription_end_date = st.date_input("Subscription End Date")
            billing_cycle = st.text_input("Billing Cycle")
            payment_status = st.text_input("Payment Status")
            product_usage = st.number_input("Product Usage", min_value=0)
            account_manager = st.text_input("Account Manager")
            customer_segment = st.text_input("Customer Segment")
            customer_feedback = st.text_area("Customer Feedback")
            
            submit_button = st.form_submit_button(label='Add Customer')

            if submit_button:
                customer = Customer(
                    customer_id=customer_id,
                    customer_name=customer_name,
                    company_name=company_name,
                    email=email,
                    phone=phone,
                    address=address,
                    subscription_plan=subscription_plan,
                    subscription_start_date=subscription_start_date,
                    subscription_end_date=subscription_end_date,
                    billing_cycle=billing_cycle,
                    payment_status=payment_status,
                    product_usage=product_usage,
                    account_manager=account_manager,
                    customer_segment=customer_segment,
                    customer_feedback=customer_feedback
                )
                customers = load_customers()
                customers.append(customer)
                save_customers(customers)
                st.success("Customer added successfully!")

    elif choice == "View Customers":
        customers = load_customers()
        if not customers:
            st.write("No customers found.")
        else:
            data = [{
                'Customer ID': customer.customer_id,
                'Customer Name': customer.customer_name,
                'Company Name': customer.company_name,
                'Email': customer.email,
                'Phone': customer.phone,
                'Address': customer.address,
                'Subscription Plan': customer.subscription_plan,
                'Subscription Start Date': customer.subscription_start_date,
                'Subscription End Date': customer.subscription_end_date,
                'Billing Cycle': customer.billing_cycle,
                'Payment Status': customer.payment_status,
                'Product Usage': customer.product_usage,
                'Account Manager': customer.account_manager,
                'Customer Segment': customer.customer_segment,
                'Customer Feedback': customer.customer_feedback
            } for customer in customers]
            
            # Create DataFrame from list of dictionaries
            df = pd.DataFrame(data)
            
            # Display the DataFrame
            st.dataframe(df)

    elif choice == "Search Customer":
        search_name = st.text_input("Enter customer name:")
        if st.button("Search"):
            customers = load_customers()
            found_customers = [customer for customer in customers if search_name.lower() in customer.customer_name.lower()]
            if not found_customers:
                st.write("No customer found.")
            else:
                data = [{
                    'Customer ID': customer.customer_id,
                    'Customer Name': customer.customer_name,
                    'Company Name': customer.company_name,
                    'Email': customer.email,
                    'Phone': customer.phone,
                    'Address': customer.address,
                    'Subscription Plan': customer.subscription_plan,
                    'Subscription Start Date': customer.subscription_start_date,
                    'Subscription End Date': customer.subscription_end_date,
                    'Billing Cycle': customer.billing_cycle,
                    'Payment Status': customer.payment_status,
                    'Product Usage': customer.product_usage,
                    'Account Manager': customer.account_manager,
                    'Customer Segment': customer.customer_segment,
                    'Customer Feedback': customer.customer_feedback
                } for customer in found_customers]
                
                # Create DataFrame from list of dictionaries
                df = pd.DataFrame(data)
                
                # Display the DataFrame
                st.dataframe(df)
    elif choice == "Delete Customer":
        delete_name = st.text_input("Enter customer name to delete:")
        if st.button("Delete"):
            # Delete the customer from the database
            delete_customer(delete_name)
            st.success("Customer deleted successfully!")

if __name__ == "__main__":
    main()
