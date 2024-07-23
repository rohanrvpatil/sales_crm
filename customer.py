class Customer:
    def __init__(self, customer_id, name, email, phone, address, notes=""):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.notes = notes

    def __str__(self):
        return (f"ID: {self.customer_id}, Name: {self.name}, Email: {self.email}, "
                f"Phone: {self.phone}, Address: {self.address}, Notes: {self.notes}")

    def to_dict(self):
        return {
            'customer_id': self.customer_id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'address': self.address,
            'notes': self.notes
        }

    #@staticmethod
    #def from_dict(data):
       # return Customer(data['customer_id'], data['name'], data['email'],
        #                data['phone'], data['address'], data['notes'])
