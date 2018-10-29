
#Remove nth character from string
string1=input("enter the string:")
n=int(input("Enter the nth character to remove:"))
fpart=string1[:n-1]
lpart=string1[n:]
newstring=fpart+lpart
print("NEW STRING : %s "%(newstring))