import pandas as pd
from faker import Faker
import random

# Initialize Faker
fake = Faker()

# Create a dictionary to hold the data
data = {
    "Customer ID": [fake.uuid4() for _ in range(100)],
    "Customer Name": [fake.name() for _ in range(100)],
    "Company Name": [fake.company() for _ in range(100)],
    "Email": [fake.email() for _ in range(100)],
    "Phone": [fake.phone_number() for _ in range(100)],
    "Address": [fake.address() for _ in range(100)],
    "Subscription Plan": [random.choice(['Basic', 'Pro', 'Enterprise']) for _ in range(100)],
    "Subscription Start Date": [fake.date_this_decade() for _ in range(100)],
    "Subscription End Date": [fake.date_this_decade() for _ in range(100)],
    "Billing Cycle": [random.choice(['Monthly', 'Annually']) for _ in range(100)],
    "Payment Status": [random.choice(['Paid', 'Due', 'Overdue']) for _ in range(100)],
    "Product Usage": [random.randint(1, 1000) for _ in range(100)],
    "Account Manager": [fake.name() for _ in range(100)],
    "Customer Segment": [random.choice(['SMB', 'Enterprise']) for _ in range(100)],
    "Customer Feedback": [fake.sentence() for _ in range(100)]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save to Excel
df.to_excel('dummy_saas_data.xlsx', index=False)
