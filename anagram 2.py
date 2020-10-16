import load_dictionary as ld

file = ld.load("dictionary.txt") #a file containing large amount of words, not a dictionary

name = input("Type your word here: ")
name_l = name.lower()
sorted_name = sorted(name_l)
anagrams = []
for word in file:
    word_l = word.lower()
    sorted_word = sorted(word_l)
    if name_l != word_l: 
        if sorted_name == sorted_word:
            anagrams.append(word)
print(anagrams)

