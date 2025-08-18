
# Task 6
days_of_the_week = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

prompt = [
        input("Student's name: ").title(),
        input("Gender: ").title(),
        input("Course track: ").title(),
        input("Current month's number(1-12): "),
        input("Current day number(1-7)(For example: 1 for Sunday): ")
        ]

name, gender, track, month, day = prompt # This unpacks the prompt tuple into individual variables.
month = int(month) - 1 # Convert month to zero-based index
day = int(day) - 1 # Convert day to zero-based index
print(f"Student name: {name}\nGender: {gender}\nCourse track: {track}\nCurrent month: {months[month]}\nCurrent day: {days_of_the_week[day]}") # This prints the student's information.
