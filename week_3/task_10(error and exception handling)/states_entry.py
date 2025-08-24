
# Tuple operations: 5 states bla bla with exception handling

states = []
while len(states) < 5:
    try:
        state = input("Enter the name of a Nigerian state: ").title()
        if not state.isalpha():
            print("Please enter a valid state name (letters only). Try again.")
            continue
        states.append(state)
    except Exception as e:
        print(f"An error occurred: {e}")
        continue
try:
    states = tuple(states)
    print(states)
    print(f"First state: {states[0]}\nLast state: {states[-1]}")

    if "Lagos" in states:
        print("Lagos is in the list of states the user entered. ")
    else:
        print("Lagos is not in the list of states the user entered. ")
    print(f"{len(states)} states were inputted by the user. ")
except Exception as e:
    print(f"An error occurred while processing states: {e}")