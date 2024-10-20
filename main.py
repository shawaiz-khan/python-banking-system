# A simple Banking System in python

"""PseudoCode:
    # Make a users dictionary
    # Get user User IDs by input
    # Check if the User ID exists or not 
    # If User ID exists ask the user that he wants to add balance or check balance or exit
    # If the User ID do not exist, ask him his/her name and ask for balance and allocate an User ID
    # If he wants to add balance then add else balance is 0 by default
    # Add the new user to the users dictionary
    # Save the users in a new File (new update)"""

import json
import uuid

users = {}
fileName = "users.json"


def generate_user_id():
    return str(uuid.uuid1())


def create_account():
    user_choice = str(input('Type "y" to Create an Account and "n" to exit: '))
    if user_choice.lower() == "y":
        user_id = generate_user_id()
        user_name = str(input("Enter your Name: "))
        current_balance = 0

        global users
        users[user_id] = {
            "user_id": user_id,
            "name": user_name,
            "balance": current_balance,
        }

        print(
            """Your Account has been created successfully!
            ID: {}
            Name: {}
            Balance: {}""".format(
                users[user_id]["user_id"],
                users[user_id]["name"],
                users[user_id]["balance"],
            )
        )

        add_data()
        print(users)

    else:
        return


def add_balance(acc_num):
    if acc_num in users:
        current_balance = float(users[acc_num]["balance"])
        print("Current Balance: {}".format(current_balance))
        new_balance = float(input("Enter money to Deposit: "))
        current_balance += new_balance
        users[acc_num]["balance"] = current_balance
        print("New Balance: {}".format(current_balance))
        add_data()
    else:
        print("No user found with this User ID.")


def check_balance(acc_num):
    if acc_num in users:
        balance = users[acc_num]["balance"]
        print(f'{users[acc_num]["name"]}, your current balance is: {balance}')
    else:
        print("No user found with this User ID.")


def add_data():
    global fileName
    with open(fileName, "w") as file:
        json.dump(users, file, indent=4)


def get_data():
    global users
    global fileName
    try:
        with open(fileName, "r") as file:
            users = json.load(file)
    except FileNotFoundError:
        users = {}
    except json.JSONDecodeError:
        users = {}


def main():
    get_data()

    while True:
        print("\n--- Banking System ---")
        print("1. Create Account")
        print("2. Add Balance")
        print("3. Check Balance")
        print("4. Exit")
        choice = int(input("Enter your Choice: "))

        if choice == 1:
            create_account()
        elif choice == 2:
            acc_num = input("Enter your User ID: ")
            add_balance(acc_num)
        elif choice == 3:
            acc_num = input("Enter your User ID: ")
            check_balance(acc_num)
        elif choice == 4:
            print("Exiting the Program...")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")


main()
