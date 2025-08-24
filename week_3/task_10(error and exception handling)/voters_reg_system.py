# Unique Voters registration with exception handling

voters = set()
while True:
    try:
        voter = input("Enter your first name and last name: ").title()
        if voter not in voters:
            if voter != "Exit":
                voters.add(voter)
        else:
            print("You have already registered. Please don't try to register more than once.")
            continue
        if voter == "Exit":
            break
    except Exception as e:
        print(f"An error occurred: {e}")
        continue
    
print(f"{voters}.\nThis gives us a total of {len(voters)} registered voters.")