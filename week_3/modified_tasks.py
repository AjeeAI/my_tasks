# Check if a given string contains the substring "python"
# string_data = "This is a sample string containing the substring 'python'".lower()
# if "python" in string_data:
#     print("The substring 'python' exists in the given string.")
# else:
#     print("The substring 'python' does not exist in the given string.")
    
    
# Check the number of vowels in a sentence

# vowels = ["a", "e", "i", "o", "u"]
# sentence = input("Enter a sentence here: ").lower()
# count = 0
# for vowel in vowels:
#     if vowel in sentence:
#         count += sentence.count(vowel)
        
# print(count)


# Check if a given string startswith "https://"
""" The use case of this particular program, at least to me might be to check if a website 
is secure by checking if it is https and not just http so as to warn users about potential 
security risks"""

string_data = "https://eportal.oauife.edu.ng"

if string_data.startswith("https://"):
    print("This url(string) starts with https://") 
else:
    print("This website is not secure. Do you still want to proceed? ")
    
    
# Name Organizer
# names = []
# while len(names) < 5:
#     name = input("Enter a name here: ").lower()
#     names.append(name)
# names.sort()
# for name in names: # Isn't it just sweet to do this?
#     print(name)
    

# print("\n".join(names)) 
"""This was what I had to use when I wasn't permitted to use loops. Glory to God, I am free now"""

# Student Score Tracker:

# student_names = []
# scores = []
# while len(student_names) < 3:
#     name = input("Please enter the student's name here: ")
#     student_names.append(name)
#     score = int(input("Enter the score for this student: "))
#     scores.append(score)

# for i in range(len(student_names)):
#     print(f"\t{student_names[i]}\t --- \t{scores[i]}")
    
# word = input("Please enter a word here: ")
# print(f"The word length is: {len(word)}")
# if word == word.upper():
#     print("The word is in uppercase. ") 
# elif word == word.lower():
#     print("The word is in lowercase. ")
# elif word == word.title():
#     print(" The word is in title case. ")
# else:
#     print("This word does not follow any specific case. ")
# print(f"This is \"{word}\" in reverse: {word[::-1]}")

# Tuple operations: 5 states bla bla

# states = []
# while len(states) < 5:
#     state = input("Enter the name of a Nigerian state: ").title()
#     states.append(state)
# states = tuple(states)
# print(states)
# print(f"First state: {states[0]}\nLast state: {states[-1]}")

# if "Lagos" in states:
#     print("Lagos is in the list of states the user entered. ")
# else:
#     print("Lagos is not in the list of states the user entered. ")
    
# print(f"{len(states)} states were inputted by the user. ")

# Simulate a football match ticket system:

seat_numbers = set(range(1, 5))

# no = 1
# while len(seat_numbers) < 5:
#      seat_numbers.add(no)
#      no += 1

# while len(seat_numbers) > 0:
#     print(seat_numbers)
#     while True:
#         booking = int(input("Choose from the available seats to book: "))
#         if booking in seat_numbers:
#             print(f"Congratulations. You have successfully booked seat {booking}")
#             seat_numbers.remove(booking)
            
#             break
#         else:
            
#             print(f"This seat, seat{booking} is no longer available")
#             print(f"Available seats are: {seat_numbers}")
# print("All seats have been taken. No more seats available.")

# Unique Voters registration

# voters = set()
# while True:
#     voter = input("Enter your first name and last name: ").title()
#     if voter not in voters:
#         if voter != "Exit":
#             voters.add(voter)
#     else:
#         print("You have already registered. Please don't try to register more than once.")
#         continue
    
#     if voter == "Exit":
#         break
    
# print(f"{voters}.\nThis gives us a total of {len(voters)} registered voters.")

# bio_data = {}
# while True:
#     student_list = []
#     name = input("Enter student's name: ").title()
#     if name  == "Exit":
#         break
#     else: 
#         age = int(input("Enter the student's age:"))
#         gender = input("Enter the gender: ")
#         bio_data["name"] = name 
#         bio_data["age"] = age
#         bio_data["gender"] = gender
        
#         courses = []
#         while True:
            
#             course = input(f"Enter course: ").title()
#             if course == "Done":
#                 break
#             else:
#                 courses.append(course)
#                 print(courses)
#         bio_data["courses"] = courses
        
#     print(bio_data)

"""

- This program collects student details, academic scores, hobbies, and guardian info, 
stores them in a nested dictionary, and performs automatic calculations and transformations 
using dictionary comprehension, tuple unpacking, and set operations.
"""
students = dict()
count = 1
    
while True:
    info = dict()
    
    basic_info = dict()
    # info["name"] = input("Enter the student's name: ").title()
    # info["age"] = int(input("Enter the student's age: "))
    # info["gender"] = input("Enter the gender of the said student: ").title()
    basic_info["Name"] = input("Enter the student's name: ").title()
    basic_info["Initials"] = "".join([n[0] for n in basic_info["Name"].split()])
    print(basic_info["Initials"])
    basic_info["Age"] = int(input("Enter the student's age: "))
    basic_info["Gender"] = input("Enter the gender of the said student: ").title()
    
    info["basic info"] = basic_info
    list_scores = int(input("Enter the number of subjects you want to scores for: "))
    scores = []
    info["Academics"] = scores
    total = 0
    
    for i in range(list_scores):
        score_info = {}
        subject = input("Enter the subject you would like to have score for: ")
        score = int(input("Enter the score for the subject: "))
        score_info[subject] = score
        scores.append(score_info)
        print(score_info)
        print(scores)
        
        for score in score_info.values():
            total += score
            avg_score = total/list_scores
        # info["Average score"] = avg_score
        score_info["Average score"] = avg_score
        print(total)
    
    hobbies = set()
    info["Hobbies"] = hobbies
    while True:
        hobby = input("Enter your hobbies one at a time: ").title()
        if hobby != "Done":
            hobbies.add(hobby)
        else:
            break
        
    hobbies = list(hobbies)
    info["Total number of hobbies"] = len(hobbies)
    guardian_info = dict()
        
    guardian_info["guardian's name"] = input(f"Enter the guardian's name for {basic_info["Name"]}: ")
    guardian_info["guardian's contact_info"] = input(f"Enter the {basic_info["Name"]} guardian's contact: ")
    info["guardian_info"] = guardian_info
    print(info)
    
    students[f"student{count}"] = info
    count += 1
    print(students)
        
    exit = input("If you done, please enter 'Done' to exit: ").title()
    if exit == "Done":
        break
    else:
        continue
hobbies = list(hobbies)
print(info)
print(students)
for key, value in students.items():
    # for key, value in value.items():
    #     print(f"{key}: {value}")
    print(f"{key}: \n{value}")
   
           