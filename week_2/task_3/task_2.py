# Task 2

attendees = input("Enter the name of the attendees. Put a space after each entry:\n")
attendees = attendees.split()
attendees = set(attendees) # Converted the entries to a set
attendees = list(attendees) # I had convert to a list before sorting because I can't rely on set() to print in a particular order
attendees.sort() # This arranges it in alphabetical order. 
print(attendees)