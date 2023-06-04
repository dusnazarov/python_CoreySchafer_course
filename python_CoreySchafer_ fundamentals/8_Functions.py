# ////////////////////////////////////
# def hello_func():  
#     pass

# print(hello_func)
# print(hello_func())

# ////////////////////////////////////
# def hello_func():
    
#     return 'Hello function!'

# print(hello_func())

# ////////////////////////////////////
# def hello_func():
#     print('Hello function!')
   
# hello_func()

# # ////////////////////////////////////
# def hello_func(greeting, name):
#     return f'{greeting}, {name} '
   
# print(hello_func('Hi', 'Elyor'))
# print(hello_func('Hi', name='Elyor'))


# # # ////////////////////////////////////
# def student_info(*args):
#     print(args)    
#     print(args[0])    
#     print(type(args))   

# student_info('Elyor', 'Dusnazarov', 'Uzbekiston')

# # # ////////////////////////////////////
# def student_info(*args):
#     print(args)    
#     print(args[0])    
#     print(args[0][0])    
#     print(type(args))    
  
# # data = ('Elyor', 'Dusnazarov', 'Uzbekiston')
# data = ['Elyor', 'Dusnazarov', 'Uzbekiston']

# student_info(*data)

# # # ////////////////////////////////////
# def student_info(**kwargs):
#     print(kwargs)   
#     print(type(kwargs))    

# student_info(first_name='Elyor', last_name='Dusnazarov', country='Uzbekistan')

# # ////////////////////////////////////
# def student_info(**kwargs):
#     print(kwargs)
#     print(kwargs.get('first_name'))       
#     print(type(kwargs))
  
# data = {"first_name":"Elyor", "last_name":"Dusnazarov", "country":"Uzbekistan"}
# student_info(**data)


# # /////////////////////////
# def student_info(*args, **kwargs):
#     print(args)   
#     print(kwargs)
#     print(kwargs.get('name'))

# courses = ['Math', 'Art']
# info = {'name': 'John', 'age': 22} 

# student_info(*courses, **info)

# ///////////////////////////////////

# Number of days per month. First value placeholder for indexing purposes.
# month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


# def is_leap(year):
#     """Return True for leap years, False for non-leap years."""

#     return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


# def days_in_month(year, month):
#     """Return number of days in that month in that year."""

#     if not 1 <= month <= 12:
#         return 'Invalid Month'

#     if month == 2 and is_leap(year):
#         return 29

#     return month_days[month]

# print(is_leap(2020))
# print(days_in_month(2020, 6))