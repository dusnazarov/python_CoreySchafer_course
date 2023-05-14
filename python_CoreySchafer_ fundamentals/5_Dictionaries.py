# # ///////////////////////////////////////////////
# student = {'name':'John', 'age':25, 'courses':['Math', 'CompSci']}

# # print(student)
# # print(student['name'])
# # print(student.get('name'))
# print(student.get('phone'))
# print(student.get('phone', 'Not Found'))


# # ///////////////////////////////////////////////
# student = {'name':'John', 'age':25, 'courses':['Math', 'CompSci']}

# student['phone'] = 941233333
# student['name'] = "Jane"

# print(student.get('phone', 'Not Found'))
# print(student)

# # ///////////////////////////////////////////////
# student = {'name':'John', 'age':25, 'courses':['Math', 'CompSci']}

# student.update({'name':'elyor', 'age':27, 'phone':1236547})


# print(student.get('phone', 'Not Found'))
# print(student)

# # ///////////////////////////////////////////////
# student = {'name':'John', 'age':25, 'courses':['Math', 'CompSci']}

# del student['age']

# print(student)

# # ///////////////////////////////////////////////
# student = {'name':'John', 'age':25, 'courses':['Math', 'CompSci']}

# age = student.pop('age')

# print(student)
# print(age)

# ///////////////////////////////////////////////
student = {'name':'John', 'age':25, 'courses':['Math', 'CompSci']}

# print(student.values())
# print(student.keys())
# print(student.items())

# for key in student:
#     print(key)

for key, value in student.items():
    print(key, value)
