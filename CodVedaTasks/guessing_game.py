import random

lowest = 1
highest = 100
attempt = 7

def guess_number():
    while True:
        try:
            guess = int(input("Please enter a number: "))

        except ValueError:
            print("Kindly Enter a Valid Number")
            continue


        if guess < lowest or guess > highest:
            print("Your guess must be between 1 and 100")
            continue

        return guess


def start_game():
    secret = random.randint(lowest, highest)
    attempt_used = 0
    print(f"Kindly guess number between {lowest} and {highest}")
    print(f"You have {attempt} attempts")

    while attempt_used < attempt:
        print(f"You have {attempt_used - attempt} attempts left")
        guess = guess_number()
        attempt_used += 1

        if guess == secret:
            print(f"Congratulations, you got it in {attempt_used} attempts")

        elif guess > secret:
            print(f"Too high you have {attempt - attempt_used} attempts left")

        else:
            print(f"Too low you have {attempt - attempt_used} attempts left")


     print(f"You ran out of chance, the secret is {secret} ")


def main():
    start_game()
    again = input("Would you like to play again? (y/n): ")
    if again != "yes":
        print("Thank you for playing")
if __name__ == "__main__":
    main()
