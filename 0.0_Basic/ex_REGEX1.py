import re

#split on , and . and white spaces
string = 'apple,pear,grapes,carrot.cabbage,veggies.fruit,yard how! you are'
word=re.split('\\s|\.,',string)
print(word)



#\D= anything but a number (a non-digit)
hword="abcdef123"
hlist = re.findall('\D', hword)
print(hlist)