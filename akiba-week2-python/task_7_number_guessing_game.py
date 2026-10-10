import random

secret_number = random.randint(1, 10)
attempts = 0
max_attempts = 5

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 10.")
print(f"You have {max_attempts} attempts to guess it.")

while attempts < max_attempts:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess == secret_number:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
        break
    elif guess < secret_number:
        print("Too low! Try a higher number.")
    else:
        print("Too high! Try a lower number.")

    print(f"Attempts remaining: {max_attempts - attempts}")

if attempts == max_attempts and guess != secret_number:
    print("Game Over!")
    print(f"The secret number was {secret_number}.")