# Prompt user to enter the distance in kilometers
# Prompt user to enter the fare per kilometer
# Calculate the total fare by multiplying distance by fare per kilometer
# Display the total fare in Naira with two decimal places

distance = input("Enter the distance in kilometers: ")
fare = input("Enter the fare per kilometer: ")
total_fare = float(distance) * float(fare)
print(f"The total fare is: ₦{total_fare:,.2f}k")