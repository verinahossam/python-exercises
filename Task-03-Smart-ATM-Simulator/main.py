# Smart ATM Simulator

# Welcome Message
message = "Welcome to the ATM Simulator"
print(message.center(40))

# Variables
pin_in_system = 1234
current_balance = 5000

# Get the PIN from the user
pin = int(input("Enter your PIN: ").strip())

# Check the PIN
if pin == pin_in_system:

    operation = int(input("Choose 1 for Withdraw or 2 for Check Balance: ").strip())

    if operation == 1:

        # Withdraw Money
        withdraw_amount = int(input("Enter the withdrawal amount: ").strip())

        if withdraw_amount > current_balance:
            print("Sorry, your balance is insufficient.")
        else:
            new_balance = current_balance - withdraw_amount
            print("Transaction completed successfully.")
            print(f"Your new balance is {new_balance}.")

    elif operation == 2:

        # Check Balance
        print(f"Your balance is {current_balance}.")

    else:
        print("Invalid choice.")

else:
    print("Incorrect PIN. Transaction denied.")
