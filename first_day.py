import random
import os

def generate_password(length=12):
    # Define character sets
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"
    symbols = "!@#$%^&*()-_+=<>?"

    # Combine all character sets
    all_characters = upper + lower + numbers + symbols

    # Generate a random password
    password = "".join(random.sample(all_characters, length))
    return password

def save_password(password):
    # Save password to a file
    file_path = "passwords.txt"
    with open(file_path, "a") as file:
        file.write(password + "\n")
    print(f"Password saved to {os.path.abspath(file_path)}")

# Main program
if __name__ == "__main__":
    print("Welcome to the Password Generator!")
    try:
        length = int(input("Enter the desired password length (minimum 8): "))
        if length < 8:
            print("Password length must be at least 8.")
        else:
            password = generate_password(length)
            print(f"Generated Password: {password}")

            save_choice = input("Do you want to save this password to a file? (y/n): ").lower()
            if save_choice == "y":
                save_password(password)
            else:
                print("Password not saved.")
    except ValueError:
        print("Invalid input. Please enter a number.")
