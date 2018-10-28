

#FIND largest number in the list
'''''
list11=[]
num=int(input("Enter no of items :"))
for i in range (1,num+1):
    n=int(input("enter number :"))
    list11.append(n)

list11.sort()
print ( "largest number is %d"  %( list11[-1]))
'''''



#GENERATE LIST OF ODD /EVEN numbers
'''''
list1=[10,20,43,65,77,99,100,333]
even=[]
odd=[]
for num in list1:
    if (num%2 == 0):
        even.append(num)
    else:
        odd.append(num)

print( "EVEN LIST :", even)
print( "ODD LIST : ", odd )
'''''