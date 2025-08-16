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