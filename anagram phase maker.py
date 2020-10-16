#this program creates possible anagrams from the input and lets user select -
#the word he want, then creates next possible word with remainig letters untill
#no more words can be created or no more letters are remaining.

import load_dictionary as ld
from collections import Counter
import sys


dic_file = ld.load("dictionary.txt")
dic_file.append("a")
dic_file.append("i")
dic_file = sorted(dic_file)



def find_anagram(ini_name,dic_file,final_phrase):
    ini_map = Counter(ini_name)
    anagrams = []
    for word in dic_file:
        test = ""
        word_map = Counter(word.lower())
        for letter in word:
            if word_map[letter] <= ini_map[letter]:
                test += letter
                if Counter(test) == word_map:
                    anagrams.append(word)
    if anagrams == []:
        error = "Sorry no anagram is formed with the remaining letter/letters"
        print(error)
        input_ini()
    else:
        choice(anagrams,ini_name,final_phrase)

    

def choice(anagrams,ini_name,final_phrase):
    temp = ini_name[:]
    print(*anagrams)
    chosen_word = input("Select a word (press # to exit]/[press @ to try again): ")
    if chosen_word in anagrams:
        limit = len(ini_name)
        finished = ""
        for letter in chosen_word:
            temp = temp.replace(letter,"",1)
        #print("chosen word is " + chosen_word)
        print("remaining letters are: "+ temp)
        final_phrase += chosen_word+" "
        
        if temp == "":
            print("final phrase is " + final_phrase)
            sys.exit()
        else:
            find_anagram(temp, dic_file,final_phrase)
        
    elif chosen_word == "@":
        input_ini()
    elif chosen_word == "#":
        sys.exit()
    else:
        print("try again")
        choice(anagrams,ini_name,final_phrase)
 
    
    
                          
                    
            
    
def input_ini():
    ini_name = input("Enter the name: ")
    ini_name = ini_name.lower()
    ini_name = ini_name.replace(" ","")
    ini_name = ini_name.replace("-","")
    final_phrase = ""
    find_anagram(ini_name,dic_file,final_phrase)
    
    

    
input_ini()
