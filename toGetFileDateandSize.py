# Use the built-in version of scandir/walk if possible, otherwise
# use the scandir module versions
import os 
import time

try:
    from os import scandir, walk
except ImportError:
    from scandir import scandir, walk

total_size = 0

txt_file = open('D:\\TEST\\BHP\\result.txt', 'w')
txt_file.write("File Name\t\t\t\t\t\tCreated Time\t\t\t\t\tModified Time\t\t\t\t\tSize(MB)"+"\n")

inputdir = "D:\TEST\BHP"
for entry in scandir(inputdir):
	if entry.is_file() and os.path.splitext(entry.name)[1].lower()==".zip":
		fp = os.path.join(inputdir, entry.name)
		txt_file.write(entry.name+"\t\t\t\t"+time.ctime(os.path.getctime(fp))+"\t\t\t"+time.ctime(os.path.getmtime(fp))+"\t\t\t"+str(os.path.getsize(fp)/(float(1024)*float(1024)))+"\n")