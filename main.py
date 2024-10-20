# A simple Banking System in python

"""PseudoCode:
    # Make a users dictionary
    # Get user account numbers by input
    # Check if the account number exists or not 
    # If account number exists ask the user that he wants to add balance or check balance or exit
    # If the account number do not exist, ask him his/her name and ask for balance and allocate an account number
    # If he wants to add balance then add else balance is 0 by default
    # Add the new user to the users dictionary
    # Save the users in a new File (new update)"""

userID = 0
users = {}


def generate_user_id():
    global userID
    userID += 1
    return userID


def create_account():
    user_choice = str(input('Type "y" to Create an Account and "n" to exit: '))
    if "y" or "Y" in user_choice:
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

        print(users)

    else:
        print("Exiting...")
        # Exit the program


def add_balance(acc_num):
    if acc_num in users:
        current_balance = float(users[acc_num]["balance"])
        print("Current Balance: {}".format(current_balance))
        new_balance = float(input("Enter money to Deposit: "))
        current_balance += new_balance
        users[acc_num]["balance"] = current_balance
        print("New Balance: {}".format(current_balance))
    else:
        print("Exiting...")


def main():
    acc_num = input("Enter your Account Number: ")

    while True:
        if acc_num.isdigit() and int(acc_num) in users:
            add_balance(int(acc_num))
            print("User Exists")
        else:
            print("User do not exist! Create an Account")
            create_account()

main()
