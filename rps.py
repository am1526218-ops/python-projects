from pickle import TRUE
import random
choices = ["rock", "paper", "scissors"]

while True:
    user = input("enter rock, paper, or scissors(or 'quit' to stop): ").lower()

    if user == "quit":
        print("game ended")
        break

    if user not in choices:
        print("invalid choice! try again.")
        continue

    computer = random.choice(choices)
    print("computer chose:", computer)

    if user == computer:
        print("it's a tie!")
    elif (user == "rock" and computer == "scissors") or\
    (user == "paper" and computer == "rock") or\
    (user == "scissors" and computer == "paper"):
        print("you win!")
    else:
        print("computer wins!")
else:
    print("you lose!")

    print()
