import random
import time
import sys

def rolling_animation():
    print("Rolling", end="", flush=True)
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print()

def roll_dice():
    input("Press Enter to roll the dice 🎲 ")
    rolling_animation()
    result = random.randint(1, 6)
    print(f"\nYou rolled a {result}!\n")

if __name__ == "__main__":
    while True:
        roll_dice()
        again = input("Roll again? (y/n): ").strip().lower()
        if again != 'y':
            print("Thanks for playing!")
            break
