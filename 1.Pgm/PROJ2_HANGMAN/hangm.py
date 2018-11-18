
#HANGMAN GAME
import random
import re

def string_index(string1,letter):
    i = 0
    ind = set()
    while i < len(string1):
        item = string1.find(letter, i, len(string1))
        i = i + 1
        if item != -1:
            ind.add(item)
        else:
            break
    return ind



with open("worddb.txt","r") as file1:
    list1=file1.readlines()
    rword1=random.choice(list1)
    hword=re.split(',|\:',rword1)[0]
    hint = re.split(',|\:', rword1)[2]
    print(hword)


print ("------------LETS PLAY !!-----------\n")
print("GUESS THE WORD:  IT HAS  "+str(len(hword))+ "  characters" )
print ('WORD:' )
print ( "*"*len(hword))

inp=input( "Enter your GUESS Letter/Word ")
user_in=inp.upper()
print(user_in)

try:
    if user_in.isalpha() == 'True'and user_in in  hword:
        string_index(hword,user_in)

except Exception:
    print ("User input wrong")