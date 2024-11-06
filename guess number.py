import random

def guess_the_number():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False

    print("Welcome to the Number Guessing Game!")
    print("I've picked a number between 1 and 100. Try to guess it!")

    while not guessed_correctly:
        try:
            # Get user input and check if it's a valid number
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            # Compare user guess with the generated number
            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                guessed_correctly = True
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
        except ValueError:
            print("Please enter a valid integer.")

# Run the game
guess_the_number()
