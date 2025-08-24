# Check the number of vowels in a sentence

vowels = ["a", "e", "i", "o", "u"]
sentence = input("Enter a sentence here: ").lower()
count = 0
for vowel in vowels:
    if vowel in sentence:
        count += sentence.count(vowel)
        
print(count)