users = {
'Students': [ 
 {'first_name':  'Michael', 'last_name' : 'Jordan'},
 {'first_name' : 'John', 'last_name' : 'Rosales'},
 {'first_name' : 'Mark', 'last_name' : 'Guillen'},
 {'first_name' : 'KB', 'last_name' : 'Tonel'}
],
'Instructors': [
 {'first_name' : 'Michael', 'last_name' : 'Choi'},
 {'first_name' : 'Martin', 'last_name' : 'Puryear'}
]
}
''' comment out working block
keyList = []
for key in users:
	keyList.append(key)
keycount = 0
count = 1
length = 0
print keyList[keycount]+'\n'
keycount += 1
for student in users['Students']:
	length = len(student['first_name'])+len(student['last_name'])
 	print count, '- '+student['first_name'], student['last_name']+' -', length
 	count += 1
print '\n'+keyList[keycount]+'\n'
for instructor in users['Instructors']:
	length = len(instructor['first_name'])+len(instructor['last_name'])
 	print count, '- '+instructor['first_name'], instructor['last_name']+' -', length
 	count += 1
 '''
keyList = []
for key in users:
	keyList.append(key)
for data in users:
	data
