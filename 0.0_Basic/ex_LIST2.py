

#select random item in list
import random
color_list = ['Red', 'Blue', 'Green', 'White', 'Black']
print(random.choice(color_list))

#merge two list
'''''
list1=[10,20,30]
list2=[55,1,2]
list3=list1+list2
print(list3)
'''''

#Find COMMON in two lists
'''''
list1=[55,56,22]
list2=[88,56,22]
list3=[]
for i in list1:
    for j in list2:
        if(i == j):
            list3.append(i)
        else:
            continue
print (list3)
'''''

#Remove duplicate words in list
a=[]
n= int(input("Enter the number of elements in list:"))
for x in range(0,n):
    element=int(input("Enter element" + str(x+1) + ":"))
    a.append(element)
b = set()
unique = []
for x in a:
    if x not in b:
        unique.append(x)
        b.add(x)
print("Non-duplicate items:")
print(unique)