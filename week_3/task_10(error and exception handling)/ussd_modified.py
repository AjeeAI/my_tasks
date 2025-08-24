
banks = ["Access", "First Bank", "Zenith", "GTB", "Wema", "EcoBank"]
password = 8995
balance = 9500

while True:
    try:
        print("\nOptions:")
        print("1: Transfer")
        print("2: Buy airtime")
        print("3: Check balance")
        print("4: Enquiry")
        print("0: Exit")

        ussdInput = input("What do you want to do today: ")

        if ussdInput == "1":
            print("\nTransfer Menu:")
            print("1: Transfer to same bank")
            print("2: Transfer to other banks")
            transInput = input("Enter option here: ")

            if transInput == "1":
                attempts = 3
                while attempts > 0:
                    entry = input("Enter the 10 digit account number: ")
                    if len(entry) == 10 and entry.isdigit():
                        amount = input("Enter amount to transfer: ")
                        try:
                            amt_int = int(amount)
                            if amt_int <= balance:
                                balance -= amt_int
                                print(f"Transfer of ₦{amt_int} to account {entry} successful.")
                                print(f"Remaining balance: ₦{balance:,}")
                                break
                            else:
                                print("Insufficient funds or invalid amount!")
                                break
                        except ValueError:
                            print("Invalid amount! Please enter a number.")
                            continue
                    else:
                        attempts -= 1
                        print(f"Invalid account number. {attempts} attempts left.")
                        if attempts == 0:
                            print("Too many invalid attempts. Returning to main menu.")
                            break

            elif transInput == "2":
                attempts = 3
                while attempts > 0:
                    print("\nSelect bank:")
                    for i, bank in enumerate(banks, start=1):
                        print(f"{i}: {bank}")
                    try:
                        entry = int(input("Enter bank number: "))
                        if 1 <= entry <= len(banks):
                            acc_attempts = 3
                            while acc_attempts > 0:
                                acc_entry = input(f"Enter the 10 digit {banks[entry-1]} account number: ")
                                if len(acc_entry) == 10 and acc_entry.isdigit():
                                    amount = input("Enter amount to transfer: ")
                                    try:
                                        amt_int = int(amount)
                                        if amt_int <= balance:
                                            balance -= amt_int
                                            print(f"Transfer of ₦{amt_int} to {banks[entry-1]} account {acc_entry} successful.")
                                            print(f"Remaining balance: ₦{balance:,}")
                                            acc_attempts = 0
                                            attempts = 0
                                            break
                                        else:
                                            print("Insufficient funds or invalid amount!")
                                            acc_attempts = 0
                                            attempts = 0
                                            break
                                    except ValueError:
                                        print("Invalid amount! Please enter a number.")
                                        continue
                                else:
                                    acc_attempts -= 1
                                    print(f"Invalid account number. {acc_attempts} attempts left.")
                                    if acc_attempts == 0:
                                        print("Too many invalid attempts. Returning to main menu.")
                                        break
                        else:
                            attempts -= 1
                            print(f"Invalid bank selection. {attempts} attempts left.")
                            if attempts == 0:
                                print("Too many invalid attempts. Returning to main menu.")
                                break
                    except ValueError:
                        attempts -= 1
                        print(f"Invalid input. {attempts} attempts left.")
                        if attempts == 0:
                            print("Too many invalid attempts. Returning to main menu.")

        elif ussdInput == "2":
            print("\nAirtime Menu:")
            print("1: Buy for self")
            print("2: Buy for others")
            airtimeInput = input("Enter option here: ")

            if airtimeInput == "1":
                amount = input("Enter amount: ")
                try:
                    amt_int = int(amount)
                    if amt_int <= balance:
                        balance -= amt_int
                        print(f"Airtime of ₦{amt_int} bought successfully for yourself.")
                        print(f"Remaining balance: ₦{balance:,}")
                    else:
                        print("Insufficient funds or invalid amount!")
                except ValueError:
                    print("Invalid amount! Please enter a number.")

            elif airtimeInput == "2":
                attempts = 3
                while attempts > 0:
                    phoneNumber = input("Enter phone number (11 digits): ")
                    if phoneNumber.isdigit() and len(phoneNumber) == 11:
                        amount = input("Enter amount: ")
                        try:
                            amt_int = int(amount)
                            if amt_int <= balance:
                                balance -= amt_int
                                print(f"Airtime of ₦{amt_int} bought successfully for {phoneNumber}.")
                                print(f"Remaining balance: ₦{balance:,}")
                                break
                            else:
                                print("Insufficient funds or invalid amount!")
                                break
                        except ValueError:
                            print("Invalid amount! Please enter a number.")
                            continue
                    else:
                        attempts -= 1
                        print(f"Invalid phone number. {attempts} attempts left.")
                        if attempts == 0:
                            print("Too many invalid attempts. Returning to main menu.")
                            break

            else:
                print("Invalid option!")

        elif ussdInput == "3":
            attempts = 3
            while attempts > 0:
                user_pass = input("Enter your password: ")
                try:
                    if int(user_pass) == password:
                        print(f"Your account balance is ₦{balance:,}")
                        break
                    else:
                        attempts -= 1
                        print(f"Incorrect password. {attempts} attempts left.")
                        if attempts == 0:
                            print("Too many invalid attempts. Returning to main menu.")
                except ValueError:
                    attempts -= 1
                    print(f"Password must be numeric. {attempts} attempts left.")
                    if attempts == 0:
                        print("Too many invalid attempts. Returning to main menu.")

        elif ussdInput == "4":
            print("\nEnquiry Menu:")
            print("1: Branch locations")
            print("2: Loan products")
            print("3: Customer care")
            enquiryInput = input("Enter option: ")

            if enquiryInput == "1":
                print("Nearest branch: Lagos Island, Marina.")
            elif enquiryInput == "2":
                print("Loan products: Personal, SME, Mortgage.")
            elif enquiryInput == "3":
                print("Customer care: Call 0700-123-4567")
            else:
                print("Invalid option!")

        elif ussdInput == "0":
            print("Thank you for banking with us. Goodbye!")
            break

        else:
            print("Please input a valid option!!!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
