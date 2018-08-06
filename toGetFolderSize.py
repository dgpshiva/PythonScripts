# Use the built-in version of scandir/walk if possible, otherwise
# use the scandir module versions
import os 

try:
    from os import scandir, walk
except ImportError:
    from scandir import scandir, walk

total_size = 0

txt_file = open('D:\\TEST\\result.txt', 'w')
txt_file.write("Folder Name\t\t\tSize(MB)"+"\n")

inputdir = "D:\\TEST"
for entry in scandir(inputdir):
	if entry.is_dir():
		search_dir = os.path.join(inputdir, entry.name)		
					
		for root, dirs, files in os.walk(search_dir, topdown='true'):
			for file in files:
				total_size+=os.path.getsize(os.path.join(root, file))
		txt_file.write(entry.name+"\t\t\t\t"+str(total_size/(float(1024) * float(1024)))+"\n")		
		total_size = 0