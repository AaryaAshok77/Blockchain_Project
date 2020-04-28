from datetime import datetime

# TODO: checking everything, like withdraw before end of rental
# TODO: add contract signing


class SmartContract:
    def __init__(self, id):
        self.id = 0
        self.client_balance = 0
        self.owner_balance = 0
        self.booking_details = BookingDetails

    def retrieve_balance(self, private_key):
        return self.client_balance 

    def withdraw_earnings(self, private_key):
        return self.owner_balance

    def client_deposit(self, ether):
        self.client_balance += ether

    def owner_deposit(self, ether):
        self.owner_balance += ether

    def allow_car_usage(self):
        self.booking_details.get_car().allow_to_use()

    def add_booking_details(self, booking_details):
        self.booking_details = booking_details

    def get_booking_details(self):
        return self.booking_details

    def end_car_rental(self):
        self.booking_details.get_car().end_rental()
    
    def get_car(self):
        return self.booking_details.get_car()


class BookingDetails:
    def __init__(self, car, price_per_day):
        self.car = car
        self.price_per_day = price_per_day
        self.no_of_days = 0
        self.rental_date = datetime.now()

    def request(self, no_of_days):
        self.no_of_days = no_of_days

    def get_summed_cost(self):
        return self.price_per_day * self.no_of_days

    def get_car(self):
        return self.car

