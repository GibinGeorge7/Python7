



#Python Program to Count the Number of Vowels Present in a String using Sets
count=0
string1=input("enter the string: ")
vowels=set("aeioua")
print (vowels)
for letter in string1:
    if letter in vowels:
        count=count+1
print ("no of vowels in STRING is :%s" %(count))