# Question 1
# This program takes an input from the user and converts it to uppercase.

entry = input("Enter info here: ")
print(entry.upper())

# Question2
# This code prints the first and last characters of the string "python".

entry = "python"
print(f"The first character is {entry[0]} and the last character is {entry[-1]}")

# Question 3
# The code receives the name and then prints out a message that includes the name received.

name = input("Enter your name: ")
message = "Hello, !"
print(f" {name}".join(message.split())) # This line splits the message using the "whitespace" and plugs in the input received into it.



# # Question 4
# This is a function supposedly to get the length without using the len() function

entry = "Adesoji"
length = entry.find(entry[-1])  + 1 # Here I used the find function to get the index of the value at the last position and then add 1 to that index because I took into account python's zero indexing.
print(F"The length of the entry is {length}")


# Task 5
# This replaces "World" with "Python" in "Hello World"

message = "Hello World"
print(message.replace("World", "Python"))

"""
Task 2
"""

# Question 6
# This program simply returns the sentence in lowercase

entry = " This is a Python file for checking"
print("python" in entry.lower())

# Question 7
# This program reverses a string without using the ([::-1]) slicing method.

entry = "Ajijolaoluwa"
print(entry[-1::-1]) # Manipulated the (start, stop, step) sequence in the slicing methods to perform the same operation that ([::-1]) would.


# Question 8
# Here I used the strip() function to remove the extra spaces on the left and right of the string.

entry = " This is my name     "
print(entry.strip())

# Question 9
"""Here to find the number of vowels in the sentence, I check the count of each vowel 
in the sentence and then add them together to get the total number of vowels in the said sentence."""

sentence = input("Enter a sentence: ")
sentence = sentence.lower()
contains_a = sentence.count("a")
contains_e = sentence.count("e")
contains_i = sentence.count("i")
contains_o = sentence.count("o")
contains_u = sentence.count("u")
total_vowels = contains_a + contains_e +contains_i + contains_o + contains_u
print(f"The sentence has {total_vowels} vowels in it.")


# Question 10
# This program convert a string "1234" to an whole number and then multiplies it by 2 and outputs it.

entry = "1234"
int_entry = int(entry)
print(int_entry * 2)

""" Task 3"""

# Question 11
# This splits a string "combination" of fruits into a list.
fruits = "apple,banana,orange"
print(fruits.split(","))

# Question 12
# This program takes an input and then splits it by doing using a newline in the place of the "whitespaces"

sentence = input("Enter a sentence: ")
word = "\n".join(sentence.split())
print(word)


# Question 13
# This code simply replaces the spaces in the string with underscores

entry = "This is a sample string"
print("_".join(entry.split()))

# Question 14
# Here I simply use the count() function to display the number of times "a" appeared in the word.

fruit = "Banana"
print(fruit.count("a"))


# Question 15
# This checks if the string begins with https:// using the startswith() function.

entry = "https://github.com/AjeeAI/Week2_task1.git"
print(entry.startswith("https://"))