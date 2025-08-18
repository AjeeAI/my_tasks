# Task 3: Seat Booking System
# Initialize an empty list
# Use list comprehension to store numbers 1 - 50
# Input for user to book a seat from the list of available seats.
# Remove already booked by using the remove() method
# The remaining seats are displayed using a print statement.
seat_numbers = []
[seat_numbers.append(x + 1) for x in range(50)]
seat_numbers = set(seat_numbers)
print(f"Available seats: {seat_numbers}")
booking = int(input("Book a seat by choosing a number from 1-50: "))
[seat_numbers.remove(booking)]
print(f"Remaining seats: {seat_numbers}")