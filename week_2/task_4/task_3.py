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