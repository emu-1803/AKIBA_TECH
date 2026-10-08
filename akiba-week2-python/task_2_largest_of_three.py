num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))


if num1 == num2 == num3:
    print("All three numbers are equal.")

elif num1 >= num2 and num1 >= num3:
    print(num1, "is the largest.")

elif num2 >= num1 and num2 >= num3:
    print(num2, "is the largest.")

else:
    print(num3, "is the largest.")