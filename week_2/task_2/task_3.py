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

