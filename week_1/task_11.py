# Prompt user to enter the amount in Naira
# Prompt user to enter the exchange rate for dollars
# Prompt user to enter the exchange rate for British pounds
# Convert the amount from Naira to dollars
# Convert the amount from Naira to pounds
# Display the converted amounts in dollars and pounds



amount = float(input("Enter the amount in Naira: "))
exchange_rate_dollars = float(input("Enter the exchange rate for dollars: "))
exchange_rate_pounds = float(input("Enter the exchange rate for Britishpounds: "))
converted_to_dollars = amount / exchange_rate_dollars
converted_to_pounds = amount/ exchange_rate_pounds

print(f"₦{amount:,.2f} is equivalent to: \n${converted_to_dollars:,.2f} \n£{converted_to_pounds:,.2f}")