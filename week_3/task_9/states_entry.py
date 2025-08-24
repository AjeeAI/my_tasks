
# Tuple operations: 5 states bla bla

states = []
while len(states) < 5:
    state = input("Enter the name of a Nigerian state: ").title()
    states.append(state)
states = tuple(states)
print(states)
print(f"First state: {states[0]}\nLast state: {states[-1]}")

if "Lagos" in states:
    print("Lagos is in the list of states the user entered. ")
else:
    print("Lagos is not in the list of states the user entered. ")
    
print(f"{len(states)} states were inputted by the user. ")