customer_name = input("Customer name: ")
product_name = input("Product name: ")
price = float(input("Price: "))
quantity = int(input("Quantity: "))

total = price * quantity

print()
print(f"Customer: {customer_name}")
print(f"Product: {product_name}")
print(f"Price: {price:.2f} ETB")
print(f"Quantity: {quantity}")
print(f"Total: {total:.2f} ETB")
print("Thank you for shopping!")