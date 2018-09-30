# Program to verify entered passwords are matching and RETRY for 3 iterations

import os
path1=os.getcwd()
#print (path)
file1 = os.path.join(path1,'test_files\\' 'pass1.txt')
#print (file1)

x=0
max=3
name = input("Please enter your name :\t")
print("Hi %s  ... Good Morning to you \n" % (name.capitalize()))
while x < max:
    passw1 = input("Enter New Password :\n")
    passw2 = input("Re-enter your New Password :\n")
    if  passw1== passw2:
        with open(file1,"w")as myfile :
            myfile.write(passw2)
            print("Password saved")
            break
    else:
        x=x+1
        print ("Please TRY again ..\n")
        if x== max:
            print("MAXIMUM %d Retries reached" % (max))

