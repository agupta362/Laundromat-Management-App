# Laundromat Management App

cost_per_pound = 0.50
tax_rate = 0.06
customers_info = {'Bfor4467': 80, 'Bhude1234': 70}


def main_menu():
    # Displays the main menu options
    print("\nPlease select an option:")
    print("1. Calculate total amount customer owes")
    print("2. Change wash price per pound or tax rate")
    print("3. View customer's spending history")
    print("4. Quit")


def check_input():
    # Validates and returns the customer's last name, phone number, and unique key
    customer_lastname = input(
        "\nEnter the last name of the customer (First letter capitalized):\t"
    )

    while not (customer_lastname[0].isupper() and customer_lastname[1:].islower()):
        customer_lastname = input(
            "Invalid format. Enter last name (First letter capitalized):\t"
        )

    customers_phone = int(input("Enter the phone number:\t"))

    while len(str(customers_phone)) < 4:
        customers_phone = int(input("Invalid phone number. Re-enter:\t"))

    key = customer_lastname + str(customers_phone % 10000)
    return customer_lastname, customers_phone, key


def calculate_total(weight, price_per_pound, tax_rate):
    # Calculates subtotal, tax, and total cost
    subtotal = weight * price_per_pound
    tax = subtotal * tax_rate
    total = subtotal + tax
    return subtotal, tax, total


def display_customer_history(customers_info):
    # Displays spending history for all customers
    print("\n--- Customer Spending History ---")
    print("Customer ID\tTotal Amount ($)")
    print("-" * 30)

    for customer_id, total_amount in customers_info.items():
        print(f"{customer_id}\t${total_amount:.2f}")


def search_customer_history():
    # Displays spending history for a specific customer
    key = check_input()[2]

    if key in customers_info:
        print(f"\nCumulative total for {key}: ${customers_info[key]:.2f}")
    else:
        print("There is no spending history for this customer.")


# Program start
print("Welcome to Laundromat Management App!")

while True:
    main_menu()
    user_input = input("\nEnter your choice (1–4):\t")

    if user_input == '1':
        key = check_input()[2]
        weight = float(input("Enter laundry weight in pounds:\t"))

        while weight < 0:
            weight = float(input("Weight must be positive. Re-enter:\t"))

        subtotal, tax, total = calculate_total(weight, cost_per_pound, tax_rate)

        print("\n--- Receipt ---")
        print(f"Subtotal:\t${subtotal:.2f}")
        print(f"Tax:\t\t${tax:.2f}")
        print("-------------------")
        print(f"Total:\t\t${total:.2f}")

        if key in customers_info:
            customers_info[key] += total
        else:
            customers_info[key] = total

        print(f"Cumulative total for {key}: ${customers_info[key]:.2f}")

    elif user_input == '2':
        print("\n1. Change wash price per pound")
        print("2. Change tax rate")
        print("3. Return to main menu")
        option = input("Select an option:\t")

        if option == '1':
            cost_per_pound = float(input("Enter new wash price per pound:\t"))

            while cost_per_pound < 0:
                cost_per_pound = float(
                    input("Price must be positive. Re-enter:\t")
                )

            print(f"New wash price per pound: ${cost_per_pound:.2f}")

        elif option == '2':
            # FIXED: clear and unambiguous tax input
            tax_input = float(
                input("Enter tax rate as a percentage (example: 6 for 6%):\t")
            )

            while tax_input < 0:
                tax_input = float(
                    input("Tax rate must be positive. Re-enter:\t")
                )

            tax_rate = tax_input / 100
            print(f"New tax rate set to {tax_rate * 100:.2f}%")

    elif user_input == '3':
        print("\n1. View all customers")
        print("2. Search for a customer")
        print("3. Return to main menu")
        option = input("Select an option:\t")

        if option == '1':
            display_customer_history(customers_info)
        elif option == '2':
            search_customer_history()

    elif user_input == '4':
        confirm = input("Are you sure you want to quit? (yes/no):\t")
        if confirm.lower().startswith('y'):
            print("\nThank you. Have a nice day!")
            break

    else:
        print("Invalid input. Please select a valid option.")
