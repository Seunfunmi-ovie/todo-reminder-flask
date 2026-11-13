def add(number_one,number_two):
    return number_one + number_two

def subtract(number_one,number_two):
    return number_one - number_two

def multiply(number_one,number_two):
    return number_one * number_two

def divide(number_one,number_two):
    if number_two == 0:
        return "cannot be divided by zero"
    return number_one/number_two


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Kindly enter a valid number")

def show_menu():
    print("Basic Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "5":
            print("Exiting...")
            break

        if choice not in("1","2","3","4"):
            print("Please enter a valid choice")
            continue



        first_number = get_number("Enter the first number: ")
        second_number = get_number("Enter the second number: ")

        if choice == "1":
            print(add(first_number,second_number))

        elif choice == "2":
            print(subtract(first_number,second_number))

        elif choice == "3":
            print(multiply(first_number,second_number))
        else:
            print(divide(first_number,second_number))


if __name__ == "__main__":
    main()