correct_pin = "1234"
attempts = 3

while attempts > 0:
    pin = input("Enter your PIN: ")

    if pin == correct_pin:
        print("PIN verified successfully.")
        break
    else:
        attempts -= 1
        print("Incorrect PIN.")
        if attempts > 0:
            print("Attempts remaining:", attempts)
        else:
            print("Your account is locked.")