# Task 1

fav_fruits = {
input("Input the name of your first favorite fruit: "),
input("Input the name of your second favorite fruit: "),
input("Input the name of your third favorite fruit: "),
input("Input the name of your fourth favorite fruit: "),
input("Input the name of your fifth favorite fruit: ")
}
print(fav_fruits)

# Task 2

attendees = input("Enter the name of the attendees. Put a space after each entry:\n")
attendees = attendees.split()
attendees = set(attendees) # Converted the entries to a set
attendees = list(attendees) # I had convert to a list before sorting because I can't rely on set() to print in a particular order
attendees.sort() # This arranges it in alphabetical order. 
print(attendees)

# Initialize an empty list
# Use list comprehension to store numbers 1 - 50
# Input for user to book a seat from the list of available seats.
# Remove already booked by using the remove() method
# The remianing seat are displayed using a print statement.
seat_numbers = []
[seat_numbers.append(x + 1) for x in range(50)]
seat_numbers = set(seat_numbers)
print(f"Available seats: {seat_numbers}")
booking = int(input("Book a seat by choosing a number from 1-50: "))
[seat_numbers.remove(booking)]
print(f"Remaining seats: {seat_numbers}")


# Task 4
# I initialized an empty set
# Use an if/else check to display a warning if the user tries to register twice and doesn't store their name more than once.
# The total number of unique votes is displayed using a print statement and len()

check_list = set()
name1 = input("Enter the voter's name: ")
if name1 not in check_list:
    check_list.add(name1)
else:
    print("This user is already registered")
name2 = input("Enter the voter's name: ")
if name2 not in check_list:
    check_list.add(name2)
name3 = input("Enter the voter's name: ")
if name3 not in check_list:
    check_list.add(name3)
print("Voter registration successful. The total of registered users is: ", len(check_list))
