class Customer:
    def __init__(
        self,
        customer_id,
        customer_name,
        company_name,
        email,
        phone,
        address,
        subscription_plan,
        subscription_start_date,
        subscription_end_date,
        billing_cycle,
        payment_status,
        product_usage,
        account_manager,
        customer_segment,
        customer_feedback,
        revenue,
    ):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.company_name = company_name
        self.email = email
        self.phone = phone
        self.address = address
        self.subscription_plan = subscription_plan
        self.subscription_start_date = subscription_start_date
        self.subscription_end_date = subscription_end_date
        self.billing_cycle = billing_cycle
        self.payment_status = payment_status
        self.product_usage = product_usage
        self.account_manager = account_manager
        self.customer_segment = customer_segment
        self.customer_feedback = customer_feedback
        self.revenue = revenue

    def __str__(self):
        return (
            f"ID: {self.customer_id}, Name: {self.customer_name}, Company: {self.company_name}, "
            f"Email: {self.email}, Phone: {self.phone}, Address: {self.address}, "
            f"Subscription Plan: {self.subscription_plan}, Start Date: {self.subscription_start_date}, "
            f"End Date: {self.subscription_end_date}, Billing Cycle: {self.billing_cycle}, "
            f"Payment Status: {self.payment_status}, Product Usage: {self.product_usage}, "
            f"Account Manager: {self.account_manager}, Segment: {self.customer_segment}, "
            f"Feedback: {self.customer_feedback}",
            f"Revenue: {self.revenue}",
        )

    def to_dict(self):
        return {
            "customer_id": self.customer_id,
            "customer_name": self.customer_name,
            "company_name": self.company_name,
            "email": self.email,
            "phone": self.phone,
            "address": self.address,
            "subscription_plan": self.subscription_plan,
            "subscription_start_date": self.subscription_start_date,
            "subscription_end_date": self.subscription_end_date,
            "billing_cycle": self.billing_cycle,
            "payment_status": self.payment_status,
            "product_usage": self.product_usage,
            "account_manager": self.account_manager,
            "customer_segment": self.customer_segment,
            "customer_feedback": self.customer_feedback,
            "revenue": self.revenue,
        }
