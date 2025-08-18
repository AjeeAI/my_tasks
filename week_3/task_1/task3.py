# Task 3: Online Store Cart Calculation 


cart_total = 0 # Initialize the variable 'cart_total' to store the total price of all items in the cart.
# Create a dictionary called 'cart' to represent the shopping cart.
# The dictionary contains:
#   - 'items': a list of product names currently in the cart.
#   - 'prices': a list of corresponding prices for each item in the 'items' list.
#   - 'cart_total': a field to store the total cost of all items, initially set to 0.
cart = {
    "items": ["Mouse", "Monitor", "Stylus pen"],
    "prices": [6500, 350000, 15000],
    "cart_total": 0
}

# for price in cart["prices"]:
#     cart_total += price
# print(cart_total)

cart_total += sum(cart["prices"]) 


cart["cart_total"] = cart_total

# Print the contents of the cart dictionary, showing items, prices, and total cost.
for key, value in cart.items():
    print(f"{key}: {value}")
