# Chossing a random number between 1 to 100
from random import randint
print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100.")

# Function to check user's guess with actual answer
def check_answer(user_guess,actual_answer):
    if user_guess>actual_answer:
        print("It's too high")
    elif user_guess<actual_answer:
        print("It's too low")
    else:
        print(f"You got it right! The answer was {actual_answer}")
answer=randint(1,100)
# print(answer)
# Function to set difficulty

# Let the user Guess the number
guess=int(input("Make a Guess: "))

# Track the number of turns and reduce by 1 if they get it wrong

# Repeat the guessing functionality if they get it wrong

# Keep prompting until the user guesses correctly
while True:
    check_answer(guess, answer)
    if guess == answer:
        break
    try:
        guess = int(input("Try again. Make a Guess: "))
    except ValueError:
        print("Please enter a valid integer.")
        # prompt again without changing the answer
        continue