import os
hompath=os.environ['HOMEPATH']
path2 = os.path.join(hompath,'Desktop','GIT','PY_local','9.test_files' )
os.chdir(path2)

#READ FILE
file1=open( "file1.txt","r")
print (file1.name)
print (file1.read())
file1.close()

#OPEN file with "WITH"
with open("file1.txt","r") as file2:
    print (file2)
    print (file2.read())


#read EACH file line into a LIST

try:
        file3=open("file0.txt")
        list1=file3.readlines()
        print(len(list1))
        print(list1[0])
        for line in list1:
            print("new line : " + line)
except Exception:
    print('There was some error in the file operations.')





#write each LINE in list to file
with  open("file1.txt", "a") as myfile:
    lines_of_text = ["a line of text", "another line of text", "a third line"]
    myfile.writelines(lines_of_text)
