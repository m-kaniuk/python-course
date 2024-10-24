"""
=================================================================================================
Rozbijanie na funkcje
"""


# Źle
def process_user_data(data):
    # Parse data
    # Validate data
    # Save data to database
    # Send confirmation email
    return


# Dobrze
def parse_data(data):
    # Parse data
    return


def validate_data(data):
    # Validate data
    return


def save_to_db(data):
    # Save data to database
    return


def send_confirmation_email(data):
    # Send email
    return


""" 
=================================================================================================
'Magiczne' liczby i stałe
"""

user_age = 10
# Źle
if user_age > 18:
    # Do something
    pass

# Dobrze
LEGAL_AGE = 18

if user_age > LEGAL_AGE:
    # Do something
    pass


""" 
=================================================================================================
Zagnieżdżenia
"""


# Źle
def process_order(order):
    if order is not None:
        if order.is_paid:
            if order.has_items:
                if order.stock_available():
                    if order.address_is_valid():
                        if order.is_express_delivery:
                            print("Processing express delivery.")
                            # dalsza logika dla przesyłki ekspresowej
                        else:
                            print("Processing standard delivery.")
                            # dalsza logika dla przesyłki standardowej
                    else:
                        print("Invalid delivery address.")
                else:
                    print("Insufficient stock.")
            else:
                print("No items in the order.")
        else:
            print("Order is not paid.")
    else:
        print("Order is None.")


# Dobrze
def process_order(order):
    if order is None:
        print("Order is None.")
        return

    if not order.is_paid:
        print("Order is not paid.")
        return

    if not order.has_items:
        print("No items in the order.")
        return

    if not order.stock_available():
        print("Insufficient stock.")
        return

    if not order.address_is_valid():
        print("Invalid delivery address.")
        return

    if order.is_express_delivery:
        print("Processing express delivery.")
        # dalsza logika dla przesyłki ekspresowej
    else:
        print("Processing standard delivery.")
        # dalsza logika dla przesyłki standardowej


""" 
=================================================================================================
Formatter
"""


# Przed
def say_hello(name):
    if name == "John":
        print("Hello, John")
    else:
        print("Hello, " + name)


def sum_numbers(a, b):
    return a + b


result = sum_numbers(5, 10)
print(result)


# Po
def say_hello(name):
    if name == "John":
        print("Hello, John")
    else:
        print("Hello, " + name)


def sum_numbers(a, b):
    return a + b


result = sum_numbers(5, 10)
print(result)


""" 
=================================================================================================
Zmienne
"""

# Dobrze
# Przykład 1: Obliczanie sumy cen produktów
item_prices = [19.99, 9.99, 4.99]
total_price = sum(item_prices)
print(f"Total price: {total_price}")

# Przykład 2: Sprawdzenie, czy użytkownik jest aktywny
user_is_active = True
if user_is_active:
    print("User is active")

# Przykład 3: Iteracja po liście użytkowników
users = ["Alice", "Bob", "Charlie"]
for user in users:
    print(f"Hello, {user}!")

# Przykład 4: Znalezienie maksymalnej wartości w liście
numbers = [10, 20, 30, 40]
max_value = max(numbers)
print(f"The maximum value is: {max_value}")


# Źle
# Przykład 1: Obliczanie sumy cen produktów
a = [19.99, 9.99, 4.99]
tp = sum(a)
print(f"Total price: {tp}")

# Przykład 2: Sprawdzenie, czy użytkownik jest aktywny
x = True
if x:
    print("User is active")

# Przykład 3: Iteracja po liście użytkowników
u = ["Alice", "Bob", "Charlie"]
for x in u:
    print(f"Hello, {x}!")

# Przykład 4: Znalezienie maksymalnej wartości w liście
l = [10, 20, 30, 40]
m = max(l)
print(f"The maximum value is: {m}")
