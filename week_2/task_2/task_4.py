# Task 4
profile = (
           input("First name: ").title(), 
           input("Age: "), 
           input("Favorite_color: ").title(), 
           input("Home town: ").title(), 
           )

first_name, age, fav_color, home_town = profile # This unpacks the profile tuple into individual variables.
print(f"User's first name is: {first_name}\nUser's age is: {age}\nFavorite color: {fav_color}\nHome town: {home_town}")
