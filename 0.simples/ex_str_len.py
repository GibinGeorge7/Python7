#find length of a string

s1=input('Enter a string\n')

def strl(str1):
	print ( "length of string is ") 
	print( len(str1))


if s1.isdigit():
	print("Sorry can't take numbers")

elif s1.isalpha():
	strl(s1)

else:
	print("input not matching expected format")



