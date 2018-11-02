import pyodbc
import sys

cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=serverName;DATABASE=databaseName;Trusted_Connection=yes')
cursor = cnxn.cursor()

txt_file = open('D:\\ValuetoSearch.txt')

txt_file_results = open('ResultsFile.txt', 'w')

for line in txt_file:
	for row in cursor.execute("SELECT columnName FROM table WHERE something = ?", line.replace('\n','')):
		txt_file_results.write(row.columnName+'\n')

cnxn.commit()
txt_file.close()
txt_file_results.close()