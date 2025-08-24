# Name Organizer with exception handling
names = []
while len(names) < 5:
    try:
        name = input("Enter a name here: ").lower()
        if not name.isalpha():
            print("Please enter a valid name (letters only). Try again.")
            continue
        names.append(name)
    except Exception as e:
        print(f"An error occurred: {e}")
        continue
names.sort()
for name in names: # Isn't it just sweet to do this?
    print(name)

# print("\n".join(names)) 
"""This was what I had to use when I wasn't permitted to use loops. Glory to God, I am free now"""
