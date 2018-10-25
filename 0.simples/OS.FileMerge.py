
# Program to  merge 3 files into a txt file with datetime format name format\

import glob2
import os
from datetime import datetime




path1=os.getcwd()
#print (path1)
path2 = os.path.join(path1,'test_files' )
#print (file1)
#change working directory
os.chdir(path2)

filenames = glob2.glob("file*")
#print(filenames)

t1=datetime.now()
filename1=t1.strftime("%Y-%m-%d_%H%M%S%f"+".txt")
#print(filename1)

for i in filenames:
    with open(i,"r") as myfile1:
        cont=myfile1.read()
        with open(filename1,"a") as myfile2:
            myfile2.write(cont)
            myfile2.write("\n")

