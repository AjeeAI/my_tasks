# Task 5: Store Inventory Update

# Initialize a dictionary called 'store' to represent the inventory.
# Each key is an item name, and its value is the quantity available in stock.
store = {"Book": 10, "Pen": 20, "Bag": 5}

# Prompt the user to view available items and enter the name of the item they wish to purchase.
# The input is converted to title case to match the keys in the store dictionary.
order = input(f"Available items are {store}\nEnter the name if the item you wish to purchase: ").title()

# Prompt the user to enter the quantity of the selected item they want to purchase.
# The input is converted to an integer.
quantity = int(input(f"Enter the quantity {order} you would like to purchase: "))

# Subtract the purchased quantity from the item's stock in the store dictionary.
store[order] -= quantity

# Print the updated store inventory.
print("Updated store inventory:")
for item, qty in store.items():
    print(f"{item}: {qty}")