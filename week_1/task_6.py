# Prompt user to enter the customer's full name
# Prompt user to enter the units consumed in kWh
# Prompt user to enter the cost per unit
# Calculate the total cost by multiplying units by cost per unit
# Display a table header with column titles
# Display a separator line
# Display the customer's name, units consumed, and total cost in a formatted row
# Display a closing separator line


name = str(input("Customer's full name: "))
units = int(input("Units consumed in kWh: "))
cost = float(input("Cost per unit: "))
total_cost = units * cost

print("__________________________________________________________")
print(f" {'Customer\'s name':<16} | {'Units consumed in kWh':<20} | {'Total cost':<10}  ")
print("------------------|-----------------------|--------------")
print(f" {name:<16} | {units:<20}  | {total_cost:<10}   ")
print("________________________________________________________")
