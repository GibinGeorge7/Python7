#search word in dctionary
# Retry 3 times if word not found
#supports case sensitive inputs


import json
from difflib import get_close_matches


data1=json.load(open("data.json"))
#print(data1)

var=input("Enter word to search in dictionary:\n")
var=var.lower()

def dict_check(f):
    return data1[f]



if var in data1.keys():
    print(dict_check(var))
elif var.title() in data1.keys():  # if user enters "texas" it will check for "Texas" in dictionary
    print (dict_check(var.title()))
elif len(get_close_matches(var,data1.keys())) > 0:
    var2=input("Did you mean the word  - %s  ?\nPlease input Y or N \n" % (get_close_matches(var,data1.keys(),n=1))[0])
    if var2=="y" or  var2=="Y":
            temp=get_close_matches(var,data1.keys(),n=1)
            print(dict_check(temp[0]))
    else:
            print("EXIT, BYE")