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
