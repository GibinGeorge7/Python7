import re

#split on , and . and white spaces
string = 'apple,pear,grapes,carrot.cabbage,veggies.fruit,yard how! you are'
word=re.split('\\s|\.,',string)
print(word)