
# Dictionary key/value
# PYTHON
# FUnctions
# READ file content

import os
hompath=os.environ['HOMEPATH']
fpath = os.path.join(hompath,'Desktop','GIT','PY_local','9.test_files' )
file1=  os.path.join(fpath,'fruits.txt')

address = ["Flat Floor Street", "18", "New York"]
pins = {"Mike":1234, "Joe":1111, "Jack":2222}

print(address[0], address[1],address[2])
pin = int(input("Enter your pin: "))

def find_in_file(f):    
    myfile = open(file1)
    fruits = myfile.read()
    fruits = fruits.splitlines()
    if f in fruits:
        return "That fruit is in the list."
    else:
        return "NEED to order FRUIT !"
            
if pin in pins.values():
    fruit = input("Enter fruit: ")
    print(find_in_file(fruit))
else:
    print("Incorrect pin!") 
    print("This info can be accessed only by: ")
    for key in pins.keys():
        print(key)
