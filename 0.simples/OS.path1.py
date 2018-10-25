
# os MODULE EXAMPLES

import os


path1=os.getcwd()
print (path1)

hompath=os.environ['HOMEPATH']
print (hompath)

path2 = os.path.join(hompath,'Desktop','GIT','PY_local','9.test_files' )
print (path2)

#change working directory
os.chdir(path2)
print (os.getcwd())