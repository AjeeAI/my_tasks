# Task 4: Unique Members Registration

name_entry = input("Please enter 3 names separated by commas: ").split(", ")
name_entry = set(name_entry)  # Convert to set to ensure uniqueness
name_dict = {name: len(name) for name in name_entry}
print(name_dict)
