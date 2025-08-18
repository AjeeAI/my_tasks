# Task 5: 

names = ("Ajee", "David", "Isaiah")
phone_numbers = ("09065440091", "09041106120", "07032731434")
contact_info = dict(zip(names, phone_numbers))
print(contact_info)
name = input("Enter a name to search for their phone number: ")
print(contact_info.get(name, "Name not found"))