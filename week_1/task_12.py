print("Welcome to Ajee's USSD Banking System")

prompt1 = "Please dial *895# to proceed: "
first_prompt = input(prompt1)

print("Options:\n1: Transfer\n2: Buy airtime\n3: Buy data\n4: Check balance\n0: Go back")
prompt2 = "Please select an option from the available options: "
option_prompt = input(prompt2)
print(f"You have chosen option {option_prompt}.")
if option_prompt == "1":
    print("You have selected Transfer.")
    transfer_amount = float(input("Enter the amount: "))
    print(f"You have chosen to transfer {transfer_amount:,.2f}.")
elif option_prompt == "2":
    print("You have selected Buy airtime.")
    airtime_Amount = float(input("Enter the amount: "))
    
    print(f"You have chosen to transfer {airtime_Amount:,.2f}.")
elif option_prompt == "3":
    print("You have selected Buy data.")
    data_Amount = float(input("Enter the amount: "))
    print(f"You have chosen to transfer {data_Amount:,.2f}.")
elif option_prompt == "4":
    print("You have selected Check balance.")
    print("Your balance is being checked.")
elif option_prompt == "0":
    print("You have selected Go back.")
    exit()
else:
    print("Invalid option selected.")