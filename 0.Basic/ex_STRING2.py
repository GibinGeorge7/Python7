"""""
#Remove nth character from string
string1=input("enter the string:")
n=int(input("Enter the nth character to remove:"))
fpart=string1[:n-1]
lpart=string1[n:]
newstring=fpart+lpart
print("NEW STRING : %s "%(newstring))
"""""


"""""
#FIND INDEX  of occuranes of  LETTER in a string

def string_index(word,letter):
    i=0
    new = set()
    while i<len(word):
        a=word.find(letter,i,len(word))
        i=i+1
        if a!= -1:
            new.add(a)

    return new

word=" how are mr walt wikey"
letter="w"
print(string_index(word,letter))
"""""

#replace string letters in positions mentioned .

#relative letter position /index
strloc={1,9}
#string to be worked on
tempstring="XXXXXXX"
#letter to replace with
letter="E"

def string_replace(tempstring,strloc,letter):
    for i in strloc:
        if i==0:
            strr = tempstring[i+1:]
            tempstring = letter + strr
            print(tempstring)

        elif i==1:
            strl = tempstring[0]
            strr = tempstring[i+1:]
            tempstring = strl+letter + strr
            print(tempstring)
        else:
            strl = tempstring[:i ]
            strr = tempstring[i+1:]
            tempstring = strl + letter + strr
            print(tempstring)

string_replace(tempstring,strloc,letter)