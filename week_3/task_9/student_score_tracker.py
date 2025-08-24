# Student Score Tracker:

student_names = []
scores = []
while len(student_names) < 3:
    name = input("Please enter the student's name here: ")
    student_names.append(name)
    score = int(input("Enter the score for this student: "))
    scores.append(score)

for i in range(len(student_names)):
    print(f"\t{student_names[i]}\t --- \t{scores[i]}")
    
word = input("Please enter a word here: ")
print(f"The word length is: {len(word)}")
if word == word.upper():
    print("The word is in uppercase. ") 
elif word == word.lower():
    print("The word is in lowercase. ")
elif word == word.title():
    print(" The word is in title case. ")
else:
    print("This word does not follow any specific case. ")
print(f"This is \"{word}\" in reverse: {word[::-1]}")