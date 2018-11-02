import shutil
import os
from datetime import date, datetime

try:
    from os import scandir, walk
except ImportError:
    from scandir import scandir, walk

txt_file = open('file names to search and move')
srcDir = "source directory"
processFileNames = []

for line in txt_file:
	processFileNames.append(line.replace('\n', ''))

for entry in scandir(srcDir):
	file = entry.name
	fp = os.path.join(srcDir, file)
	modDate = datetime.fromtimestamp(os.path.getmtime(fp))
	date1 = datetime.strptime('03/10/2015', "%d/%m/%Y")
	if file in processFileNames:
		if modDate >= date1:
			filename = file.split('.', 1)[0]+'_1'
			fileext = file.split('.', 1)[1]
			os.rename(os.path.join(srcDir,file), os.path.join(srcDir, filename+'.'+fileext))
			shutil.move(os.path.join(srcDir, filename+'.'+fileext), 'destination directory')