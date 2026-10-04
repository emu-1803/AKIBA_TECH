name = input("Name: ")
weight = float(input("Weight in kilograms: "))
height = float(input("Height in meters: "))

bmi = weight / (height * height)

print(f"Name: {name}")
print(f"Weight: {weight} kg")
print(f"Height: {height} m")
print(f"BMI: {bmi:.2f}")