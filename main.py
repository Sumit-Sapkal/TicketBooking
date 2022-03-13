import random


SEAT_NUMBERS = set()
PRN = set()

class User:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

        print(f"{self.name} created.")

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}"

class Ticket:
    def __init__(self, source, destination, user: User):
        self.user = user
        self.prn = -1
        self.source: string = source 
        self.destination: string = destination
        self.seat_number = -1

    def generate_ticket(self):
        self.prn = random.randint(100, 200)
        self.seat_number = random.randint(1,10)
        
        return self.seat_exists()
        # print(PRN, SEAT_NUMBERS, self.prn, self.seat_number)

    def update_ticket(self, seat_number=False, prn=False):
        if seat_number:
            current_seat_number = random.randint(1,10)
            if current_seat_number in SEAT_NUMBERS:
                return self.update_ticket(seat_number=True)
            SEAT_NUMBERS.add(current_seat_number)
            self.seat_number = current_seat_number
        if prn:
            current_prn = random.randint(100,200)
            if current_prn in PRN:
                return self.update_ticket(prn=True)
            PRN.add(current_prn)
            self.prn = current_prn

    def seat_exists(self):
        if len(SEAT_NUMBERS)== 10:
            print("Seats are full!")
            exit()
            return
        if self.prn in PRN:
            self.update_ticket(prn=True)
            print("True for PRN")
            # return self.seat_exists()
        if self.seat_number in SEAT_NUMBERS:
            self.update_ticket(seat_number=True)
            print("True for seat number")
            # return self.seat_exists()
        if self.seat_number not in SEAT_NUMBERS:
            SEAT_NUMBERS.add(self.seat_number)
        if self.prn not in PRN:
            PRN.add(self.prn)


    def __str__(self):
        return f"PRN: {self.prn}, Seat: {self.seat_number}, Source: {self.source}, Destination: {self.destination}"


class App:
    # Runs 1
    def create_user(self):
        username = input("Enter Your Name: ")
        phone = input("Enter Phone Number: ")
        user = User(name = username, phone = phone)
        return self.create_ticket(user=user)

    # Runs 2
    def create_ticket(self, user: User):
        source = input("Enter your station: ")
        destination = input("Enter your destination: ")
        confirmation = input(f"CONFIRM: {source} -> {destination} (Y/n): ")
        
        if confirmation.lower() == "y":
            ticket = Ticket(user=user, source=source, destination=destination)
            ticket.generate_ticket()
            print(ticket)

if __name__ == "__main__":
    while True:
        App().create_user()
        print(PRN, SEAT_NUMBERS)
    # App().create_user()
    