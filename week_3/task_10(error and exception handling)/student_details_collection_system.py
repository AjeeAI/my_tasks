"""

- This program collects student details, academic scores, hobbies, and guardian info, 
stores them in a nested dictionary, and performs automatic calculations and transformations 
using dictionary comprehension, tuple unpacking, and set operations.
"""
students = dict()
count = 1
    
hobbies = set()
while True:
    try:
        info = dict()
        basic_info = dict()
        basic_info["Name"] = input("Enter the student's name: ").title()
        basic_info["Initials"] = "".join([n[0] for n in basic_info["Name"].split()])
        print(basic_info["Initials"])
        basic_info["Age"] = int(input("Enter the student's age: "))
        basic_info["Gender"] = input("Enter the gender of the said student: ").title()
        info["basic info"] = basic_info
        while True:
            try:
                list_scores = int(input("Enter the number of subjects you want to scores for: "))
                if list_scores <= 0:
                    print("Please enter a positive number.")
                    continue
                break
            except ValueError:
                print("Please enter a valid number.")
        scores = []
        info["Academics"] = scores
        total = 0
        for i in range(list_scores):
            score_info = {}
            subject = input("Enter the subject you would like to have score for: ")
            while True:
                try:
                    score = int(input("Enter the score for the subject: "))
                    break
                except ValueError:
                    print("Please enter a valid score (number).")
            score_info[subject] = score
            scores.append(score_info)
            print(score_info)
            print(scores)
            for score_val in score_info.values():
                total += score_val
                avg_score = total/list_scores
            score_info["Average score"] = avg_score
            print(total)
        info["Hobbies"] = hobbies
        while True:
            hobby = input("Enter your hobbies one at a time: ").title()
            if hobby != "Done":
                hobbies.add(hobby)
            else:
                break
        hobbies_list = list(hobbies)
        info["Total number of hobbies"] = len(hobbies_list)
        guardian_info = dict()
        guardian_info["guardian's name"] = input(f"Enter the guardian's name for {basic_info['Name']}: ")
        guardian_info["guardian's contact_info"] = input(f"Enter the {basic_info['Name']} guardian's contact: ")
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
    except Exception as e:
        print(f"An error occurred: {e}")
        continue
hobbies_list = list(hobbies)
print(info)
print(students)
for key, value in students.items():
    print(f"{key}: \n{value}")
hobbies = list(hobbies)
print(info)
print(students)
for key, value in students.items():
    # for key, value in value.items():
    #     print(f"{key}: {value}")
    print(f"{key}: \n{value}")
   
           