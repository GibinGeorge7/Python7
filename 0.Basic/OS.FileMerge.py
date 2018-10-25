
# Program to  merge 3 files into a txt file with datetime format name format\

import glob2
import os
from datetime import datetime



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

