# # Question 4
# This is a function supposedly to get the length without using the len() function

entry = "Adesoji"
length = entry.find(entry[-1])  + 1 # Here I used the find function to get the index of the value at the last position and then add 1 to that index because I took into account python's zero indexing.
print(F"The length of the entry is {length}")
