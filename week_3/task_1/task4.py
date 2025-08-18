# Task 4: Student Record

# Create an empty dictionary to store student information.
student = dict()

# Prompt the user to enter their name and store it in the dictionary under the key "name".

student["name"] = input("Enter your name: ")

# Prompt the user to enter their age, convert it to an integer, and store it under the key "age".
student["age"] = int(input("Enter your age: "))

# Assign a list of scores to the student under the key "scores".
student["scores"] = [92, 80, 95]

# Calculate the average score by dividing the sum of scores by the number of scores.
avg_score = sum(student["scores"])/len(student["scores"])

# Determine if the student has passed by checking if the average score is at least 50.
student["passed"] = avg_score >= 50


# Check if the student is a teenager (age between 13 and 19, inclusive) and store the result.
student["teenager"] = ( student["age"] >= 13 and student["age"] <=19)

# Loop through all key-value pairs in the student dictionary and print them.
for key, value in student.items():
    print(f"{key}: {value}")
