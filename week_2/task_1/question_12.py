# Question 12
# This program takes an input and then splits it by doing using a newline in the place of the "whitespaces"

sentence = input("Enter a sentence: ")
word = "\n".join(sentence.split())
print(word)
