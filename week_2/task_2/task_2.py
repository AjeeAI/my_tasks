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