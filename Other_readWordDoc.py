#txt=open("D:\\from_server\\word_parse\\test\\test.docx", 'r')

#with open("D:\\from_server\\word_parse\\test\\test.docx", 'r') as thefile:
#	for linef in thefile:
#		theline=linef.encode('utf-8')
#		print (theline)

import win32com.client
app = win32com.client.Dispatch('Word.Application')
doc = app.Documents.Open('<path_to_file>\\<file_name>.docx')
print (doc.Content.Text)
app.Quit()
