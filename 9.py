#9.  Implement a program to create a dictionary of students with Registration number and names. Perform the two operations, insert and delete. 
dict = {'181040001':'aaa', '181040002':'bbb', '181040003':'ccc', '181040004':'ddd'}
print("created dictionary:\n",dict)
dict['181040005']='eee'
print("Dictionary after inserting",dict)
del dict['181040001'] 
print("Dictionary after deletion",dict)