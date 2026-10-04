employee_name = input("Employee name: ")
basic_salary = float(input("Basic salary: "))
transport_allowance = float(input("Transport allowance: "))
food_allowance = float(input("Food allowance: "))

gross_salary = basic_salary + transport_allowance + food_allowance

print()
print(f"Employee: {employee_name}")
print(f"Basic Salary: {basic_salary:.2f} ETB")
print(f"Transport Allowance: {transport_allowance:.2f} ETB")
print(f"Food Allowance: {food_allowance:.2f} ETB")
print(f"Gross Salary: {gross_salary:.2f} ETB")