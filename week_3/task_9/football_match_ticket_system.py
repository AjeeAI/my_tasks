# Simulate a football match ticket system:

seat_numbers = set(range(1, 50))

no = 1
while len(seat_numbers) < 50:
     seat_numbers.add(no)
     no += 1

while len(seat_numbers) > 0:
    print(seat_numbers)
    while True:
        booking = int(input("Choose from the available seats to book: "))
        if booking in seat_numbers:
            print(f"Congratulations. You have successfully booked seat {booking}")
            seat_numbers.remove(booking)
            
            break
        else:
            
            print(f"This seat, seat{booking} is no longer available")
            print(f"Available seats are: {seat_numbers}")
print("All seats have been taken. No more seats available.")
