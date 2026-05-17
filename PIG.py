import random

def roll_dice():
    return random.randint(1, 6)

winning_score = 50

while True:
    players = input("enter number of players(2 - 4):")
    if players.isdigit():
        players = int(players)

        if 2 <= players <= 4:
            break
        else:
            print("please enter a number between 2 and 4.")
    else:
        print("invalid input! enter a number.")

player_scores = [0] * players

while max(player_scores) < winning_score:
    
    for player in range(players):

        print("\n" + "-" * 30)
        print(f"player {player + 1}'s Turn")
        print(f"total score: {player_scores[player]}")
        print("-"  *30)

        current_score = 0

        while True:
            choice = input("roll the dice? (y/n):").lower()
            if choice != "y":
                break

            dice = roll_dice()
            print(f"you rolled: {dice}")

            if dice == 1:
                print("oops! you rolled a 1.")
                print("turn over.! no points added.")
                current_score = 0
                break

            current_score += dice
            print(f"current turn score: {current_score}")

            player_scores[player] += current_score

            print(f"total score of player {player + 1}: {player_scores[player]}")

            if player_scores[player] >= winning_score:
                break

            winner = player_scores.index(max(player_scores))

            print("\n" + "=" * 30)
            print(f"player {winner +1} wins the game!")
            print(f"winning score: {player_scores[winner]}")
            print("=" * 40)



