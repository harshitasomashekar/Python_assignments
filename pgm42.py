#42. Read the regno and name in the file, create a dictinary of these data.
'''import csv
with open('StudentFile.txt','r') as csvfile:
	students_reader=csv.reader(csvfile)
	dictionary_form=dict(students_reader)
	print("File Contents in Dictionary format are:\n",dictionary_form)'''
f = open('StudentFile.txt','r')
answer={}
for line in f:
	k,v = line.strip().split('=')
	answer[k.strip()]=v.strip()
f.close()
