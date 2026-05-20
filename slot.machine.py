import random
import time

symbols = ["A", "B", "c", "D", "7"]

balance = 100

print("=== SLOT MACHINE ===")
print("starting balance: $100")

while balance > 0:

    print(f"/nCurrent Balance: ${balance}")

    bet = input("enter your bet amount:")
    
    if not bet.isdigit():
        print("enter a valid number")
        continue

    bet = int(bet)
    if bet <= 0:
        print("bet must be greater than 0!")
        continue

    if bet > balance:
        print("not enough balance!")
        continue

    print("/nspinning...")
    time.sleep(1)

    slot1 = random.choice(symbols)
    slot2 = random.choice(symbols)
    slot3 = random.choice(symbols)

    print(f"/n {slot1} | {slot2} | {slot3}")

    if slot1 == slot2 == slot3:
        winnings = bet * 5 
        balance += winnings
        print(f"JACKPOT! you win ${winnings}!")

    elif slot1 == slot2 or slot2 == slot3 or slot1 == slot3:
        winnings = bet * 2
        balance += winnings
        print(f"Nice! you win ${winnings}!")

    else:
        balance -= bet
        print(f"you lost ${bet}!")

        if balance <= 0:
            print("\nGame over! you ran out of money!")
            break

        play_again = input("\nplay again? (y/n):").lower()

        if play_again != "y":
            break

        print(f"\nFinal balance: ${balance}")
        print("thanks for playing!")