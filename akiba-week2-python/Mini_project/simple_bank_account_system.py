balance = 1000
correct_pin = "1234"
attempts = 3
transactions = 0

while attempts > 0:
    pin = input("Enter your PIN: ")

    if pin == correct_pin:
        print("PIN correct!")
        print("Welcome to Akiba Bank.")
        break
    else:
        attempts -= 1
        print("Incorrect PIN.")
        print("Attempts remaining:", attempts)

if attempts == 0:
    print("Too many incorrect attempts.")
    print("Your account is locked.")

else:
    while True:
        print("\n===== AKIBA BANK =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            print("Your current balance is:", balance, "Birr")

        elif choice == "2":
            try:
                amount = float(input("Enter deposit amount: "))

                if amount > 0:
                    balance += amount
                    transactions += 1
                    print("Deposit successful!")
                    print("Your new balance is:", balance, "Birr")
                else:
                    print("Deposit amount must be greater than zero.")

            except ValueError:
                print("Invalid amount. Please enter a number.")

        elif choice == "3":
            try:
                amount = float(input("Enter withdrawal amount: "))

                if amount <= 0:
                    print("Withdrawal amount must be greater than zero.")
                elif amount > balance:
                    print("Insufficient balance!")
                else:
                    balance -= amount
                    transactions += 1
                    print("Withdrawal successful!")
                    print("Your new balance is:", balance, "Birr")

            except ValueError:
                print("Invalid amount. Please enter a number.")

        elif choice == "4":
            print("Transactions made:", transactions)
            print("Thank you for using Akiba Bank!")
            print("Goodbye!")
            break

        else:
            print("Invalid option.")
            print("Please choose a valid option.")