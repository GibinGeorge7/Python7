
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


def string_replace(tempstring,strloc,letter):
    for i in strloc:
        if i==0:
            strr = tempstring[i+1:]
            tempstring = letter + strr


        elif i==1:
            strl = tempstring[0]
            strr = tempstring[i+1:]
            tempstring = strl+letter + strr

        else:
            strl = tempstring[:i ]
            strr = tempstring[i+1:]
            tempstring = strl + letter + strr

    return tempstring

def match():
    print("")
    print("SUCCESS!!!")
    print("*** YOU GUESSED THE WORD RIGHT in %s ATTEMPTS !!***" % (j))
    exit()

with open("worddb.txt","r") as file1:
    list1=file1.readlines()
    rword1=random.choice(list1)
    hword=re.split(',|\:',rword1)[0]
    hlist=re.findall('\D',hword)
    hint = re.split(',|\:', rword1)[2]
    #print(hword)


print ("------------LETS PLAY !!-----------\n")
print("GUESS THE WORD:  IT HAS  "+str(len(hword))+ "  characters" )
print("YOU HAVE 10 ATTEMPTS TO GUESS THE WORD")
print ('HANGMAN WORD:' )
print ( "*"*len(hword))

tempstring="*"*len(hword)

for j in range(1,11,1):
        print("")
        inp = input(" TRY %s : Enter your GUESS Letter/Word:\t "%(j))
        if inp.upper() == hword:
            match()

        elif inp.isalpha():
            try:
                if j == 5:
                    print("")
                    print("*****HINT******")
                    print(hint)

                user_in=inp.upper()
                if  user_in in  hlist:
                    #GET MATCHING LETTER INDEXES in WORD
                    strloc=string_index(hword,user_in)
                    #REPLACE MATCHING INDEXES WITH LETTER
                    tempstring=string_replace(tempstring,strloc,user_in)
                    print( "GOOD !! .Your Guess is Correct : %s \t"% (tempstring))
                    if tempstring == hword:
                        match()


            except Exception:
                print ("User input wrong")
        else:
            print("")
            print("*****USER INPUT EXPECTED : LETTER or WORD ***")

if j==10:
    print("MAX ATTEMPT LIMIT REACHED!! .. GOOD LUCK NEXT TIME ")