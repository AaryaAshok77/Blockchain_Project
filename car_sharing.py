from contract import SmartContract, BookingDetails

class Owner:
    def __init__(self):
        self.contract = SmartContract()
        self.balance = float(input("Enter initial balance for Owner: "))

    def add_car_to_rent(self):
        car_info = input("Enter the car you want to add: ")
        day_price = float(input("Enter the daily rental price for the car: "))
        self.contract.add_booking_details(BookingDetails(Car(car_info), day_price))

    def deploy(self, blockchain):
        eth = float(input("Enter the amount of Ether to deploy: "))
        self.balance -= eth
        self.contract.owner_deposit(eth)
        blockchain.add_new_transaction(self.contract)

    def withdraw_earnings(self):
        self.balance += self.contract.withdraw_earnings()

    def allow_car_usage(self):
        self.contract.allow_car_usage()

    def encrypt_and_store_details(self, blockchain):
        blockchain.mine()

class Customer:
    def __init__(self):
        self.contract = SmartContract()
        self.balance = float(input("Enter initial balance for Customer: "))

    def request_book(self, blockchain):
        eth = float(input("Enter the amount of Ether for booking: "))
        self.contract = blockchain.get_unconfirmed_transactions()[0]
        self.contract.client_deposit(eth)
        self.balance -= eth

    def pass_number_of_days(self):
        days_no = int(input("Enter the number of days for rental: "))
        booking_details = self.contract.get_booking_details()
        booking_details.request(days_no)
        
    def retrieve_balance(self):
        self.balance += self.contract.retrieve_balance()

    def end_car_rental(self):
        self.contract.end_car_rental()

    def access_car(self):
        self.contract.get_car().access()


class Car:
    def __init__(self, car_info):
        self.car_info = car_info
        self.is_rented = False
        self.allowed_to_use = False

    def access(self):
        print("Car has been accessed")
        self.is_rented = True

    def end_rental(self):
        self.is_rented = False

    def allow_to_use(self):
        self.allowed_to_use = True
