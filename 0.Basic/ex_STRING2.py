"""""
#Remove nth character from string
string1=input("enter the string:")
n=int(input("Enter the nth character to remove:"))
fpart=string1[:n-1]
lpart=string1[n:]
newstring=fpart+lpart
print("NEW STRING : %s "%(newstring))
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