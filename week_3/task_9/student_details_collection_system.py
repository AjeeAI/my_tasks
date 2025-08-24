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
   
           