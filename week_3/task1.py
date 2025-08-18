
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))


# print(f"{num1} == {num2} : {num1 == num2}")
# """ This compares the values for num1 and num2 and if they are the same, it displays 'True' if not it displays 'False' """

# print(f"{num1} != {num2} : {num1 != num2}") 
# """ 
# This checks if the values for num1 and num2 are not equal to each other and if so displays 'True' 
# """
# print(f"{num1} > {num2} : {num1 > num2}")
# """ 
# This checks if the value for num1 is greater than that of num2 and if so displays 'True' 
# """
# print(f"{num1} < {num2} : {num1 < num2}")
# """ 
# This checks if the value for num1 is less than that of num2 and if so displays 'True' 
# """




# """ 1.  This compraison check can be used to check if the password entered by a user matches their signup password stored in the database"""
# """ 2. It can also be used for cases where we have to check if the name of a username a user entered is the same as the one in the database."""
# """ 3. In cybersecurity, we might have to check if the hashes of a file before and after transit is the same to verify that the file has not been tampered with or modified in any way."""




# dbUsername = "Adesoji Ajijolaoluwa"
# dbPassword = "Ajee"

# print("Login details".center(80))

# print("-" * 80)
# name_entry = input("Enter your username: ")
# password_entry = input("Enter your password here") 


# if (name_entry == dbUsername) and (password_entry == dbPassword):
#     print("Entry matches that in database.\nUser logged in")
# else:
#     if (name_entry != dbUsername) and (password_entry == dbPassword):
#         print("Data match error.\nPlease check the username entered and try again.")
#     elif (name_entry == dbUsername) and (password_entry != dbPassword):
#         print("Data match error.\nPlease check the password entered and try again.")
#     else: 
#         print("None of the details entered(Username and password) are correct")


# Task 2

"""
The code receives inputs of name, age and score from the user and 
determines their eligibility by checking if the said individual is older 
than 18 and has a score greater than 70.
"""
# name = input("Enter your name: ") # This gets the name from the user.
# age = int(input("Enter your age: ")) # This gets the age input from the user.
# score = int(input("Enter your test score: ")) # This gets an input for score from the user.

# eligibility = (age > 18) and (score > 70) # Checks if age is less than 18 and score > 70 to determine the user's eligibility.
# print(f"Candidate: {name}\nAge: {age}\nScore: {score}\nEligible: {eligibility}")



# Adaptation

# citizenship = input("What country are you from: ").title()
# enrollment = input("Are you a full time undergradute in a recognized Nigerian university: ").title()
# scholarship_status = input("Are you currently receiving any scholarship from an entity in the Oil and gas industry(Enter Yes or No): ").title()
# scores = [int(input(" Input the scores for the 5 relevant courses: ")) for score in range(5) ]

# avg_score = sum(scores)/len(scores)
# print(f"This is your average score: {avg_score}")

# Eligibility = (citizenship == "Nigeria") and (enrollment == "Yes") and (scholarship_status == "No") and (avg_score >= 60)
# print(Eligibility)


# # Task 3: Online Store Cart Calculation 

# cart_total = 0
# cart = {
#     "items": ["Mouse", "Monitor", "Stylus pen"],
#     "prices": [6500, 350000, 15000],
#     "cart_total": 0
# }

# # for price in cart["prices"]:
# #     cart_total += price
# # print(cart_total)

# cart_total += sum(cart["prices"])
# # print(cart_total)

# cart["cart_total"] = cart_total

# # print(cart)
# for key, value in cart.items():
#     print(f"{key}: {value}")

# # Task 4: Student Record

# student = dict()

# student["name"] = input("Enter your name: ")
# student["age"] = int(input("Enter your age: "))

# student["scores"] = [92, 80, 95]

# avg_score = sum(student["scores"])/len(student["scores"])
# student["passed"] = avg_score >= 50


# student["teenager"] = ( student["age"] >= 13 and student["age"] <=19 and student["age"] <=19)


# for key, value in student.items():
#     print(f"{key}: {value}")

# Task 5: Store Inventory Update

store = {"Book": 10, "Pen": 20, "Bag": 5}
order = input("Enter the name if the item you wish to purchase: ")
quantity = int(input(f"Enter the quantity {order} you would like to purchase: "))
