import os
import time
# set the filename by system time
ISOTIMEFORMAT='%Y%m%d%H%M%S'
filename='./temp/'+str(time.strftime(ISOTIMEFORMAT))+'.dat'

# set the default path
path='./temp'

# default unit is M
def gen_file(path,size):
    file=open(path,'w')
    file.seek(1024*1024*size)
    file.write('\x00')
    file.close()
size=raw_input("Enter the size(M):")

# if the catalogue doesn't exist, create it
flag=os.path.isdir(path)
if not flag:
    os.mkdir(path)

gen_file(filename,float(size))

