from blockchain import Blockchain
from car_sharing import Owner, Car, Customer

def show_balance(cust_balance, owner_balance):
    print(f"***\nCustomer balance: {cust_balance} \nOwner balance: {owner_balance}\n***")

def show_rental_cost(cost):
    print("Rental cost: ", cost)

def start():
    blockchain = Blockchain()
    owner = Owner()
    customer = Customer()

    while True:
        print("\n1. Show Balance")
        print("2. Deploy Blockchain")
        print("3. Add Car to Rent")
        print("4. Request Booking")
        print("5. Encrypt and Store Details")
        print("6. Allow Car Usage")
        print("7. Access Car")
        print("8. End Car Rental and Show Rental Cost")
        print("9. Withdraw Earnings")
        print("10. Retrieve Balance")
        print("11. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            show_balance(customer.balance, owner.balance)
        elif choice == '2':
            owner.deploy(blockchain)
        elif choice == '3':
            owner.add_car_to_rent()
        elif choice == '4':
            customer.request_book(blockchain)
            customer.pass_number_of_days()  # Pass the number of days after booking
            show_rental_cost(owner.contract.get_booking_details().get_summed_cost())  # Show Rental Cost after booking
        elif choice == '5':
            owner.encrypt_and_store_details(blockchain)
        elif choice == '6':
            owner.allow_car_usage()
        elif choice == '7':
            customer.access_car()
        elif choice == '8':
            customer.end_car_rental()
            show_rental_cost(owner.contract.get_booking_details().get_summed_cost())  # Show Rental Cost after rental ends
        elif choice == '9':
            owner.withdraw_earnings()
        elif choice == '10':
            customer.retrieve_balance()
        elif choice == '11':
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == '__main__':
    start()
