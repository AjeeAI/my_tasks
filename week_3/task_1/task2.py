# Task 2: Scholarship Eligibility Checker

"""
The code receives inputs of name, age and score from the user and 
determines their eligibility by checking if the said individual is younger 
than 18 and has a score greater than 70.
"""
name = input("Enter your name: ") # This gets the name from the user.
age = int(input("Enter your age: ")) # This gets the age input from the user.
score = int(input("Enter your test score: ")) # This gets an input for score from the user.

eligibility = (age < 18) and (score > 70) # Checks if age is less than 18 and score > 70 to determine the user's eligibility.
print(f"Candidate: {name}\nAge: {age}\nScore: {score}\nEligible: {eligibility}")

# For this inputs: 
"""**Task1**
- Explain each output of the program below.
- Give 3 usecases or cenarios where you can apply the program below.
- Write the code for 1 of the 3 use cases.
"""
# The Eligibility Check is false because both the age and the score are not within the required limits.

# Adaptation

citizenship = input("What country are you from: ").title()
enrollment = input("Are you a full time undergradute in a recognized Nigerian university: ").title()
scholarship_status = input("Are you currently receiving any scholarship from an entity in the Oil and gas industry(Enter Yes or No): ").title()
scores = [int(input(" Input the scores for the 5 relevant courses: ")) for score in range(5) ]

avg_score = sum(scores)/len(scores)
print(f"This is your average score: {avg_score}")

Eligibility = (citizenship == "Nigeria") and (enrollment == "Yes") and (scholarship_status == "No") and (avg_score >= 60)
print(Eligibility)
