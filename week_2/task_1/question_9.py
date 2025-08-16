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
