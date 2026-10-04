usd_amount = float(input("USD Amount: "))
exchange_rate = float(input("Exchange Rate: "))

etb_amount = usd_amount * exchange_rate

print(f"USD Amount: {usd_amount}")
print(f"Exchange Rate: 1 USD = {exchange_rate} ETB")
print(f"ETB Amount: {etb_amount:.2f} ETB")