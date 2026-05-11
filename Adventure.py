print("welcome to choose your own adventure!")

name = input("what is your name?")

print("hello", name)
print("you are standing in front of a dark forest.")

choice1 = input("Do you enter the forest? (yes/no) ")

if choice1 == "yes":
    print("you walkinto the forest.")

    choice2 = input("you see a river and a cave.where do you go?(river/cave): ")
    if choice2 == "river":
        print("you go the river.")

        choice3 = input("Do you swim or build a boat? (swim/boat) ")
        if choice3 == "swim":
            print("a crocodile attacks you.game over!")
        elif choice3 == "boat":
            print("you saftely cross the river and find a treasure !")
        else:
            print("invalid choice")

    elif choice2 == "cave":
        print("you enter the cave.")

        choice3 = input("you find a sleeping dragon.Fight or run? (fight/run)") 
        if choice3 == "fight":
            print("the dragon defeats you.Game over!")
        elif choice3 == "run":
            print("you escape saftely and survive!")
        else:
            print("invalid choice")

elif choice1 == "no":
    print("you stay home safetly.The adventure ends.")
else:
    print("invalid choice.")
