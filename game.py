
import random

number = random.randint(1, 100)
attempts = 0

print(" Guess the Number Game!")

while True:
    guess = int(input("Enter your guess: "))
    attempts = attempts + 1

    if guess < number:
        print(" Too low!")
    elif guess > number:
        print(" Too high!")
    else:
        print(" Correct guess!")
        print("Attempts taken:", attempts)
        break


