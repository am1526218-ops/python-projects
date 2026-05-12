import random
import string
import json
import os

# ---------------- MASTER PASSWORD ----------------

MASTER_PASSWORD = "admin123"

login = input("Enter Master Password: ")

if login != MASTER_PASSWORD:
    print("Wrong Password!")
    exit()

# ---------------- LOAD DATA ----------------

FILE_NAME = "passwords.json"

if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r") as file:
        data = json.load(file)
else:
    data = {}

# ---------------- FUNCTIONS ----------------

def save_data():
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


def add_password():
    website = input("Enter Website/App Name: ")
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    data[website] = {
        "username": username,
        "password": password
    }

    save_data()
    print("Password Saved Successfully!")


def view_passwords():
    if not data:
        print("No Passwords Saved.")
        return

    for website, info in data.items():
        print("\n------------------")
        print("Website :", website)
        print("Username:", info["username"])
        print("Password:", info["password"])


def search_password():
    website = input("Enter Website Name: ")

    if website in data:
        print("\nFound!")
        print("Username:", data[website]["username"])
        print("Password:", data[website]["password"])
    else:
        print("No Data Found.")


def generate_password():
    length = int(input("Enter Password Length: "))

    characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    password = "".join(random.choice(characters) for _ in range(length))

    print("Generated Password:", password)


# ---------------- MAIN LOOP ----------------

while True:
    print("\n====== PASSWORD MANAGER ======")
    print("1. Add Password")
    print("2. View Passwords")
    print("3. Search Password")
    print("4. Generate Password")
    print("5. Exit")

    choice = input("Choose Option: ")

    if choice == "1":
        add_password()

    elif choice == "2":
        view_passwords()

    elif choice == "3":
        search_password()

    elif choice == "4":
        generate_password()

    elif choice == "5":
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice")