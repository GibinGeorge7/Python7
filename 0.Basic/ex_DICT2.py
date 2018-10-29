
#Program to Create a Dictionary with Key as First Character and Value as Words Starting with that Character

string1=input("Enter the string:")
list1=[]
list2=[]
d={}
list1=string1.split()
for word in list1:
    string2=word[0]
    list2.append(string2)

d=dict(zip(list2,list1))
print(d)
