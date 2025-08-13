# fav_dishes = []
# for i in range(3):
#     fav_dish  = input("Enter the name of your favourite dish: ")
#     fav_dishes.append(fav_dish)
# # print(fav_dishes)

# dishes = tuple(fav_dishes)
# print(dishes)
# [print(dish) for dish in dishes]

"""Task 1
Done according to guidelines

"""
dishes = (
          input("Input your favorite dish: ").title(),
          input("Input your favorite dish: ").title(),
          input("Input your favorite dish: ").title()
          ) # This is basically like a list of inputs.
print(", ".join(dishes)) # This prints the dishes in a single line and separates them using commas.
print("\n".join(dishes)) # This prints the dishes in separate lines.


# # Task 2

# friends_names = []
# for i in range(5):
#     friends_name = input("Enter your bestfriend's name: ")
#     friends_names.append(friends_name)
# # print(friends_names)

# friends = tuple(friends_names)
# print(friends[::-1])


"""
Task 2 done according to guideline
"""
friends = (
            input("Input your bestfriend's name: ").title(),
            input("Input your another bestfriend's name: ").title(),
            input("Input your another bestfriend's name: ").title(),
            input("Input your another bestfriend's name: ").title(),
            input("Input your another bestfriend's name: ").title()
)
print(friends[::-1]) # This prints the bestfriends entry in reverse order.

# # Task 3

# states_list = []
# for  i in range(5):
#     state = input("Enter a Nigerian state: ")
#     states_list.append(state)

# print(states_list)

# states = tuple(states_list)
# print(states[0], states[-1])
# if ("Lagos" in states) == True:
#     print("Yes")
# else:
#     print("No")


# print(len(states))



"""
Task 3 done as per the guidelines given.
"""
states = (
          input("Input the name of Nigerian state: ").title(),
          input("Input the name of another Nigerian state: ").title(),
          input("Input the name of another Nigerian state: ").title(),
          input("Input the name of another Nigerian state: ").title(),
          input("Input the name of another Nigerian state: ").title(),
          )


print(f"First: {states[0]}\nLast: {states[-1]}") # This prints the first and last state in the tuple.
print("Lagos" in states) # This checks if "Lagos" is in the states tuple.
print(f"The list of states contains {len(states)} states.") # This prints the length of the tuple, which is the number of states in it.


# Task 4
profile = (
           input("First name: ").title(), 
           input("Age: "), 
           input("Favorite_color: ").title(), 
           input("Home town: ").title(), 
           )

first_name, age, fav_color, home_town = profile # This unpacks the profile tuple into individual variables.
print(f"User's first name is: {first_name}\nUser's age is: {age}\nFavorite color: {fav_color}\nHome town: {home_town}")


# Task 5
shopping_list = ( 
                input("Input first item: ").title(),
                input("Input second item: ").title(),
                input("Input third item: ").title()
                     )

shopping_list = list(shopping_list) # This converts the tuple to a list so that we can extend it with more items.
extra_items = [
            input("Input first extra item: ").title(),
            input("Input second extra item: ").title()
                ]
shopping_list.extend(extra_items) # This extends the shopping list with extra items. Extend was used instead of append so as to avoid nested "lists".
# print(shopping_list)
shopping_list = tuple(shopping_list) # This converts the list back to a tuple.
print("|".join(shopping_list)) # This prints the shopping list items separated by "|".


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
