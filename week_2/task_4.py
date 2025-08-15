bio_data = {
    "name": input("Enter the name: "),
    "age": input("Enter user's name: "),
    "gender": input("Enter your gender: "),
    "courses": input("Enter your courses: ").split()
}

for key, values in bio_data.items():
    print(f"{key}:\t {values}")
    