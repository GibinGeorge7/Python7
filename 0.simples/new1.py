# check frruit in "sample.txt"

fru=input('Enter name of fruit:\n')

def chck_fruit(f):
	myfile=open("sample.txt")
	fruits=myfile.read()
	fruits=fruits.splitlines()
	myfile.close()
	#print (fruits)
	if fru in  fruits:
		print (" we have fruit in list")
	else:
		print (" out of stock,adding to list")


chck_fruit(fru)
