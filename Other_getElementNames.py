from lxml import etree
from io import StringIO

txt_file = open('enter text file name where you want to write the output', 'w')

tree = etree.parse('enter location of xsd file name to parse')
root = tree.getroot()
for child in root:
	if (child.get('name') == "node name") and ("complexType" in child.tag) :
		nroot = child
		for element in nroot.iter():
			if 'element' in element.tag:
				txt_file.write(element.get('name')+'\n')