# Task 1:

bio_data = {
    "name": input("Enter the name: "),
    "age": input("Enter user's name: "),
    "gender": input("Enter your gender: "),
    "courses": input("Enter your courses: ").split()
}

for key, values in bio_data.items():
    print(f"{key}:\t {values}")


# Task 2

item_data = {
    "Items": [
        "Rice", "Spaghetti", "Yam", "Indomie"
    ],
    "Prices": [input("Enter the price of Rice: "),
               input("Enter the price of Spaghetti: "),
               input("Enter the price of Yam: "),
                input("Enter the price of indomie: ")
               ]
}
item_dict = dict(zip(item_data["Items"], item_data["Prices"]))
print(item_dict)
for key, values in item_dict.items():
    print(f"{key}:\t {values}")



# Task 3: Days and Activities Pairing
all_days = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")

chosen_days_input = input("Enter any three days of the week separated by commas: ")
chosen_days = [day.strip().capitalize() for day in chosen_days_input.split(",")]

activities_input = input(f"Enter activities for {', '.join(chosen_days)} separated by commas: ")
activities = [activity.strip() for activity in activities_input.split(",")]

# Pair chosen days and activities using dictionary comprehension and zip
day_activity_dict = {day: activity for day, activity in zip(chosen_days, activities)}

print("Day and Activity Pairing:")
print(day_activity_dict)

# Task 4: Unique Members Registration

name_entry = input("Please enter 3 names separated by commas: ").split(", ")
name_entry = set(name_entry)  # Convert to set to ensure uniqueness
name_dict = {name: len(name) for name in name_entry}
print(name_dict)

# Task 5: 

names = ("Ajee", "David", "Isaiah")
phone_numbers = ("09065440091", "09041106120", "07032731434")
contact_info = dict(zip(names, phone_numbers))
print(contact_info)
name = input("Enter a name to search for their phone number: ")
print(contact_info.get(name, "Name not found"))