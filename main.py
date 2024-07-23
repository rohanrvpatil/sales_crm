from crm import CRM
from customer import Customer
import file_operations as fo
import api_operations as ao

def main():
    crm = CRM()

    #crm.customers refers to the customers list which is a part of state of CRM class
    crm.customers = fo.load_customers()

    while True:
        print("\nCustomer Relationship Management System")
        print("1. Add Customer")
        print("2. View Customers")
        print("3. Search Customer")
        print("4. Delete Customer")
        print("5. Exit")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                name = input("Enter customer name: ")
                email = input("Enter customer email: ")
                phone = input("Enter customer phone: ")
                address = input("Enter customer address: ")
                notes = input("Enter any notes: ")
                
                # Fetch additional customer info from API
                #profile_info = ao.fetch_customer_profile(email)
                #notes += f" | Profile Info: {profile_info}"

                customer = Customer(None, name, email, phone, address, notes)
                crm.add_customer(customer)
            elif choice == 2:
                crm.view_customers()
            elif choice == 3:
                search_name = input("Enter the name to search: ")
                crm.search_customer(search_name)
            elif choice == 4:
                delete_name = input("Enter the name to delete: ")
                crm.delete_customer(delete_name)
            elif choice == 5:
                fo.save_customers(crm.customers)
                print("Customers saved. Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
