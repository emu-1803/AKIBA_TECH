while True:
    number = int(input("Enter a number: "))

    if number == 0:
        print("Zero")
    elif number % 2 == 0:
        print("The number is Even")
    else:
        print("The number is Odd")