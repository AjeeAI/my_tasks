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
