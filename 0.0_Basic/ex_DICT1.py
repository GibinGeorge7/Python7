'''''
#dictionary
dict1={"bob":123,"pop":777,"mike":888}
print(dict1.keys())
print(dict1.values())
print (dict1["bob"])

#update dictionary
dict1["nike"] = 234
print (dict1)
dict2={"a":3,"s":6}
dict1.update(dict2)
print (dict1)

#remove dict key
del dict1["pop"]
print (dict1)



# Program to Generate a Dictionary that Contains Numbers (between 1 and n) in the Form (x,x*x).
n=int(input("Enter a number:"))
d={x:x*x for x in range(1,n+1)}
print(d)
'''''

#Python Program to Count the Frequency of Words Appearing in a String Using a Dictionary
string1=input("Enter string :")
list1=[]
list2=[]
list1=string1.split()

for word in  list1:
  list2.append([list1.count(word)])

d=dict(zip(list1,list2))
print(d)