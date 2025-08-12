# Prompt user to enter the name of the market
# Prompt user to enter the number of traders in the market
# Display a sentence stating the market name and number of traders
# Prompt user to enter the total revenue generated in the market
# Format the revenue with commas for readability
# Display the formatted revenue value
# Display a sentence stating the total revenue generated in the market


market_name = str(input("Enter the name of the market: "))
no_of_traders = int(input("Enter the number of traders in the market: "))
revenue = float(input("Enter the total revenue generated in the market: "))
revenue_formatted = f"{revenue:,}"
print(revenue_formatted)
print(f"The total revenue generated in {market_name} is ₦{revenue_formatted}k.")