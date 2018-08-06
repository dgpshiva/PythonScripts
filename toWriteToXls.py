import xml.etree.ElementTree as ET
import os 

try:
    from os import scandir, walk
except ImportError:
    from scandir import scandir, walk

import xlsxwriter


workbook=xlsxwriter.Workbook('nameOfXlsFile.xlsx')
worksheet=workbook.add_worksheet()

row = 0
col = 0

srcDir = "srcDirOfXmls"

for entry in scandir(srcDir):
	file = entry.name
	tree = ET.parse(os.path.join(srcDir, file))
	root = tree.getroot()
	for child in root:
		if 'something' in child.tag:
			nroot = child
			for child in nroot:
				if 'something' in child.tag:					
					var1 = child.text
				if 'something' in child.tag:
					var2 = child.text
				if 'something' in child.tag:
					var3 = child.text

	worksheet.write(row, col, var1+' '+var2)
	col = col + 1
	worksheet.write(row, col, var3)
	row = row + 1
	col = 0

workbook.close()