class Customer:
    def __init__(self):
        super().__init__()
        self.name = ""
        self.address = ""
        self.phone_number = ""

    def get_details(self):
        self.name = input("Enter name: ")
        self.address = input("Enter address: ")
        self.phone_number = input("Enter phone number: ")


class Room:
    def __init__(self):
        super().__init__()
        self.room_charge = 0
        self.room_type = ""

    def book_room(self):
        print("---ROOMS OPTIONS---")
        print("1. Standard (Rs 1000/day))")
        print("2. Deluxe (Rs 2000/day))")
        print("3. Suite (Rs 4000/day))")

        choice = int(input("Enter Room Type: "))
        days = int(input("Enter days: "))
        if (choice == 1):
            self.room_type = "Standard"
            self.room_charge = 1000*days

        elif (choice == 2):
            self.room_type = "Deluxe"
            self.room_charge = 2000*days
        elif (choice == 3):
            self.room_type = "Suite"
            self.room_charge = 4000*days
        else:
            print("Invalid Choice")
        print(f"Room Booked: {self.room_type}")
        print(f"Room Charge: {self.room_charge}")


class Restaurant:
    def __init__(self):
        super().__init__()
        self.food_bill = 0

    def order_food(self):
        while (True):
            print("---FOOD MENU---")

            print("1. Tea (Rs 20)")
            print("2. Breakfast (Rs 120)")
            print("3. Lunch (Rs 150)")
            print("4. Dinner (Rs 100)")
            print("0. Back to Main Menu")

            ch = int(input("Enter your choice:"))
            if ch == 1:
                self.food_bill += 20
            elif ch == 2:
                self.food_bill += 120
            elif ch == 3:
                self.food_bill += 150
            elif ch == 4:
                self.food_bill += 100
            elif ch == 0:
                break
            else:
                print("Invalid choice")
        print(f"Food Bill Rs {self.food_bill}")


# Multiple inheritance
# "The inheritance is still multiple because the child inherits from multiple parent classes.
# Each parent calls super().__init__() so Python can follow the Method Resolution Order (MRO) and initialize every parent exactly once.
# The chain of constructor calls may look like multilevel inheritance during execution, but the inheritance relationship itself remains multiple inheritance."
# Hotel
# ↓
# Customer
# ↓
# Room
# ↓
# Restaurant
# ↓
# object
# Inheritance diagram → Multiple inheritance.
# Constructor call order (MRO) → A chain.
# Three parents → one child
# (Customer, Room, Restaurant) → (Hotel)
# Inside Customer
# class Customer:
#     def __init__(self):
#         super().__init__()
# does not mean
# "Call my parent."
# Customer has no explicit parent except object.
# Instead, super() means:
# "Call the next class in the MRO."
# The MRO is

# Hotel
# ↓
# Customer
# ↓
# Room
# ↓
# Restaurant
# ↓
# object

# Customer's  super().__init__() calls   → Room.__init__()
# Room's  super().__init__() calls       → Restaurant.__init__()
# Restaurant's super().__init__() calls  →  object.__init__()
# Now every constructor has run
class Hotel(Customer, Room, Restaurant):
    def __init__(self):
        super().__init__()

    def show_bill(self):
        total = self.room_charge+self.food_bill
        print("\n---Bill Summary---")
        print(f"Customer Name: {self.name}")
        print(f"Room Type: {self.room_type}")
        print(f"Room Charge: {self.room_charge}")
        print(f"Food Bill: {self.food_bill}")
        print(f"Total Bill: {total}")


hotel = Hotel()
while True:
    print("\n=== HOTEL MANAGEMENT SYSTEM ===")
    print("1. Enter Customer Details")
    print("2. Room Book")
    print("3. Order Food")
    print("4. Generate Bill")
    print("5. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        hotel.get_details()
    elif choice == 2:
        hotel.book_room()
    elif choice == 3:
        hotel.order_food()
    elif choice == 4:
        hotel.show_bill()
    elif choice == 5:
        print("Thank you, Visit us Again! 😊")
        break
    else:
        print("Invalid Choice, Try again")
