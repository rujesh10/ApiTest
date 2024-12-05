import random
import os

options = ["None", "Iphone", "100$", "None", "None", "None"]

def choose_option():
    output = random.choice(options)
    print(f"Congratulations! You got {output}.")

if __name__ == "__main__":
    print("Welcome to the Lottery Game!")
    while True:  # Start an infinite loop
        save_choice = input("Would you like to start the game? (y/n): ").strip().lower()
        if save_choice == "y":
            choose_option()
        elif save_choice == "n":
            print("Thanks for playing! Goodbye!")
            break  # Exit the loop
        else:
            print("Invalid input. Please enter 'y' to play or 'n' to exit.")
