# Name Organizer
names = []
while len(names) < 5:
    name = input("Enter a name here: ").lower()
    names.append(name)
names.sort()
for name in names: # Isn't it just sweet to do this?
    print(name)

# print("\n".join(names)) 
"""This was what I had to use when I wasn't permitted to use loops. Glory to God, I am free now"""
