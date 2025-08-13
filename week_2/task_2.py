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
dishes = (input("Input your favorite dish: "),
          input("Input your favorite dish: "),
          input("Input your favorite dish: ")
          )
print(", ".join(dishes))


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
    input("Input your bestfriend's name: "),
    input("Input your another bestfriend's name: "),
    input("Input your another bestfriend's name: "),
    input("Input your another bestfriend's name: "),
    input("Input your another bestfriend's name: ")
)
print(friends[::-1])

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

states = (input("Input the name of Nigerian state: "),
          input("Input the name of another Nigerian state: "),
          input("Input the name of another Nigerian state: "),
          input("Input the name of another Nigerian state: "),
          input("Input the name of another Nigerian state: "),
          )
print(f"First: {states[0]}\nLast: {states[-1]}")
# Task 4

profile = (input("First name: "), input("Age:"), input("Favorite_color: "), input("Home town: "), )
first_name, age, fav_color, home_town = profile
print(f"User's first name is: {first_name}\nUser's age is: {age}\nFavorite color: {fav_color}\nHome town: {home_town}")


# Task 5
shopping_list_tuple = ( input("Input first item: "),
    input("Input second item: "),
    input("Input third item: ")
    
    )

shopping_list = list(shopping_list_tuple)
extra_items = [
    input("Input first extra item: "),
    input("Input second extra item: ")
]
shopping_list.extend(extra_items)
# print(shopping_list)
shopping_list = tuple(shopping_list)
print("|".join(shopping_list))


# Task 6
days_of_the_week = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

prompt = [
    input("Student's name: "),
    input("Gender: "),
    input("Course track: "),
    input("Current month's number: "),
    input("Current day number(For example: 1 for Sunday): ")
]

name, gender, track, month, day = prompt
month = int(month) - 1
day = int(day) - 1
print(f"Student name: {name}\nGender: {gender}\nCourse track: {track}\nCurrent month: {months[month]}\nCurrent day: {days_of_the_week[day]}")