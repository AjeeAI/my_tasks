"""
I  am creating som,ething similar to a typical banking ussd system.
It has multiple options for different operations the user might want to perform.
"""

print("Options:\n1: Transfer\n2: Buy airtime\n3: Check balance\n4:Enquiry\n0: Go back")

ussdInput = input("What do you want to do today: ")
if int(ussdInput) == 1:
    print("1: Transfer to same bank\n2: Transfer to other banks")
    transInput = input("Enter option here: ")
elif int(ussdInput) == 2:
    print("1: Buy for self\n2: Buy for others")
    airtimeInput = input("Enter option here: ")
elif int(ussdInput) == 3:
    print("1: Enter password")
    password = input("Enter your password: ")
    if int(password) == 8995:
        print("Your account balance is #9,500")
elif int(ussdInput) == 4:
    print("What would you like to make an enquiry about? ")
else: 
    print("Please input a valid option!!!")

        

  