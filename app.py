import streamlit as st

import pandas as pd
import matplotlib.pyplot as plt

from src.customer import Customer
from src.file_operations import save_customers, load_customers, delete_customer


from src.plot import PieChart
from src.plot import BarChart
from src.plot import LineChart


def main():
    st.title("Customer Relationship Management")

    menu = [
        "Add Customer",
        "View Customers",
        "Search Customer",
        "Delete Customer",
        "Perform EDA",
        "Graphs",
    ]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Add Customer":
        with st.form(key="add_customer_form"):
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
            revenue = st.number_input("Revenue")

            submit_button = st.form_submit_button(label="Add Customer")

            if submit_button:
                new_customer_data = {
                    "customer_id": customer_id,
                    "customer_name": customer_name,
                    "company_name": company_name,
                    "email": email,
                    "phone": phone,
                    "address": address,
                    "subscription_plan": subscription_plan,
                    "subscription_start_date": subscription_start_date,
                    "subscription_end_date": subscription_end_date,
                    "billing_cycle": billing_cycle,
                    "payment_status": payment_status,
                    "product_usage": product_usage,
                    "account_manager": account_manager,
                    "customer_segment": customer_segment,
                    "customer_feedback": customer_feedback,
                    "revenue": revenue,
                }

                customers = load_customers()
                new_customer_df = pd.DataFrame([new_customer_data])

                combined_df = pd.concat([customers, new_customer_df], ignore_index=True)
                save_customers(combined_df)
                st.success("Customer added successfully!")

    elif choice == "View Customers":
        customers = load_customers()
        if customers.empty:
            st.write("No customers found.")
        else:
            st.dataframe(customers)

    elif choice == "Search Customer":
        search_name = st.text_input("Enter customer name:")
        if st.button("Search"):
            customers = load_customers()

            filtered_df = customers.loc[customers["customer_name"] == search_name]

            if filtered_df.empty:
                st.write("No customer found.")
            else:
                st.dataframe(filtered_df)

    elif choice == "Delete Customer":
        delete_name = st.text_input("Enter customer name to delete:")
        if st.button("Delete"):
            # Delete the customer from the database
            delete_customer(delete_name)
            st.success("Customer deleted successfully!")

    elif choice == "Perform EDA":
        customers = load_customers()

        if customers.empty:
            st.write("No customer found.")
        else:
            summary = customers.describe()
            st.write(summary)

    elif choice == "Graphs":

        customers = load_customers()

        # Customer Distribution by Segment
        customer_counts = customers["customer_segment"].value_counts()
        pie_chart = PieChart(customer_counts, "Customer Distribution by Segment")
        pie_chart.plot()

        # Subscription Plan Distribution
        subscription_counts = customers["subscription_plan"].value_counts()
        bar_chart = BarChart(
            subscription_counts,
            "Subscription Plan Distribution",
            "Subscription Plan",
            "Count",
        )
        bar_chart.plot()

        # Aggregate revenue by month
        revenue_trend = (
            customers.set_index("subscription_start_date")["revenue"]
            .resample("M")
            .sum()
        )

        line_chart = LineChart(
            revenue_trend, "Revenue Trend Over Time", "Date", "Total Revenue"
        )
        line_chart.plot()


if __name__ == "__main__":
    main()
