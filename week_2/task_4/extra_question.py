# Student Information Program (Multiple Students Version)

# Prompt the user to enter the total number of students whose information will be recorded.
num_students = int(input("Enter number of students to record: "))

# Initialize an empty list that will store the profile dictionaries for all students.
students = []

# Loop through the range of student count to collect data for each student individually.
for i in range(num_students):
    print(f"\n--- Entering details for Student {i+1} ---")

    # --- Personal Information Section ---
    # Request the student's full name, remove leading/trailing spaces, and capitalize each word.
    name = input("Enter student's full name: ").strip().title()
    # Ask for the student's age and convert the input to an integer.
    age = int(input("Enter student's age: "))
    # Get the student's gender, clean up the input, and format it with the first letter capitalized.
    gender = input("Enter student's gender: ").strip().title()

    # --- Academic Information Section ---
    # Define the subjects as a tuple, representing the fixed subjects for all students.
    subjects = ("Math", "English", "Science")

    # For each subject, prompt the user to enter the student's score, convert it to float, and store in a tuple.
    scores = tuple(float(input(f"Enter score for {sub}: ")) for sub in subjects)

    # Create a dictionary that maps each subject to its corresponding score using zip and dictionary comprehension.
    scores_dict = {sub: sc for sub, sc in zip(subjects, scores)}

    # --- Guardian Information Section ---
    # Request the guardian's name, clean up the input, and format it properly.
    guardian_name = input("Enter guardian's name: ").strip().title()
    # Ask for the guardian's phone number and remove any extra spaces.
    guardian_phone = input("Enter guardian's phone number: ").strip()

    # --- Hobbies Section ---
    # Prompt the user to enter hobbies separated by commas.
    hobbies_input = input("Enter hobbies (comma separated): ")
    # Split the input string into individual hobbies, clean each one, capitalize, and remove duplicates using set.
    hobbies = list(set(h.strip().title() for h in hobbies_input.split(",")))

    # --- Calculated Values Section ---
    # Generate the student's initials by taking the first letter of each word in the name and converting to uppercase.
    initials = "".join(word[0].upper() for word in name.split())
    # Calculate the average score by dividing the sum of scores by the number of subjects.
    average_score = sum(scores) / len(scores)
    # Count the total number of unique hobbies entered.
    hobbies_count = len(hobbies)

    # --- Student Profile Construction ---
    # Organize all collected and calculated data into a nested dictionary for the current student.
    student_profile = {
        "personal": {
            "name": name,
            "age": age,
            "gender": gender,
            "initials": initials
        },
        "academic": {
            "subjects": subjects,
            "scores": scores,
            "scores_dict": scores_dict,
            "average": average_score
        },
        "guardian": {
            "name": guardian_name,
            "phone": guardian_phone
        },
        "hobbies": {
            "list": hobbies,
            "count": hobbies_count
        }
    }

    # Add the completed student profile dictionary to the main students list.
    students.append(student_profile)

# --- Display Section ---
# Loop through all student profiles and print their details in a formatted manner.
for idx, student in enumerate(students, start=1):
    print("\nSTUDENT RECORD", idx, "\n" + "-"*30)
    print(f"Name: {student['personal']['name']}")
    print(f"Age: {student['personal']['age']}")
    print(f"Gender: {student['personal']['gender']}")
    print(f"Initials: {student['personal']['initials']}\n")

    print("Subjects & Scores:")
    # Print each subject and its corresponding score for the student.
    for sub, sc in student['academic']['scores_dict'].items():
        print(f"- {sub}: {sc}")
    print(f"Average Score: {student['academic']['average']:.2f}\n")

    print("Guardian:")
    print(f"- Name: {student['guardian']['name']}")
    print(f"- Phone: {student['guardian']['phone']}\n")

    print("Hobbies:")
    print(", ".join(student['hobbies']['list']))
    print(f"Total Hobbies: {student['hobbies']['count']}")