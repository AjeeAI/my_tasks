
item_data = {
    "Items": [
        "Rice", "Spaghetti", "Yam", "Indomie"
    ],
    "Prices": [input("Enter the price of Rice: "),
               input("Enter the price of Spaghetti: "),
               input("Enter the price of Yam: "),
                input("Enter the price of indomie: ")
               ]
}
item_dict = dict(zip(item_data["Items"], item_data["Prices"]))
print(item_dict)
for key, values in item_dict.items():
    print(f"{key}:\t {values}")
