
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))


print(f"{num1} == {num2} : {num1 == num2}")
""" This compares the values for num1 and num2 and if they are the same, it displays 'True' if not it displays 'False' """

print(f"{num1} != {num2} : {num1 != num2}") 
""" 
This checks if the values for num1 and num2 are not equal to each other and if so displays 'True' 
"""
print(f"{num1} > {num2} : {num1 > num2}")
""" 
This checks if the value for num1 is greater than that of num2 and if so displays 'True' 
"""
print(f"{num1} < {num2} : {num1 < num2}")
""" 
This checks if the value for num1 is less than that of num2 and if so displays 'True' 
"""




""" 1.  This comparison check can be used to check if the password entered by a user matches their signup password stored in the database"""

""" 
 2. It can be used to check for cases where we want to monitor certain activities for example: 
 if we want to check if the voltage of power supply exists in a range of given values and does not exceed a certain threshold.
 """
""" 3. In cybersecurity, we might have to check if the hashes of a file before and after transit is the same to verify that the file has not been tampered with or modified in any way."""




dbUsername = "Adesoji Ajijolaoluwa"
dbPassword = "Ajee"

print("Login details".center(80))

print("-" * 80)
name_entry = input("Enter your username: ")
password_entry = input("Enter your password here") 


if (name_entry == dbUsername) and (password_entry == dbPassword):
    print("Entry matches that in database.\nUser logged in")
else:
    if (name_entry != dbUsername) and (password_entry == dbPassword):
        print("Data match error.\nPlease check the username entered and try again.")
    elif (name_entry == dbUsername) and (password_entry != dbPassword):
        print("Data match error.\nPlease check the password entered and try again.")
    else: 
        print("None of the details entered(Username and password) are correct")
