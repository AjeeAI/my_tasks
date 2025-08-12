# Prompt user to enter the price of the item
# Convert the entered price to a floating-point number
# Display the price formatted in Naira with two decimal places


price = str(input("Enter the price of garri per paint: "))
price_to_float = float(price)
print(f"The price of garri per paint is ₦{price_to_float:,.2f}k.")