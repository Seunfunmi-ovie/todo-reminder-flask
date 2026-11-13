def celsius_to_fahrenheit(temp):
    fahrenheit = (temp * 9 / 5) + 32
    return fahrenheit

def fahrenheit_to_celsius(temp):
    celsius = (temp - 32) * 5 / 9
    return celsius


def kilo_to_mile(kilo):
    miles = (kilo * 0.6214)
    return miles

def meter_to_kilo(miles):
    kilo = (miles / 0.6214)
    return kilo


def kilogram_to_pound(mile):
    pound = mile * 2.2046
    return pound

def pounds_to_kilogram(mile):
    kilogram = (mile/2.2046)
    return kilogram


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Try a valid number")


def show_menu():
    print("1. calculate fahrenheit")
    print("2. calculate celsius")
    print("3. calculate kilo")
    print("4. calculate meter")
    print("5. kilograms to pounds")
    print("6. pounds to kilogram")
    print("7, Existing.....")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "7":
            print("Exiting...")
            break

        if choice not in ("1", "2", "3", "4","5","6"):
            print("Kindly enter a valid choice: ")
            continue

        number = get_number("Enter your number: ")

        if choice == "1":
            print(celsius_to_fahrenheit(number))

        elif choice == "2":
            print(fahrenheit_to_celsius(number))

        elif choice == "3":
            print(kilo_to_mile(number))

        elif choice == "4":
            print(meter_to_kilo(number))

        elif choice == "5":
            print(kilogram_to_pound(number))

        else:
            print(pounds_to_kilogram(number))





if __name__ == "__main__":
    main()






