
# #////////////////////////////////////////
# class Employee:
#     num_of_emps = 0
#     raise_amt = 1.04  
      
#     def __init__(self,first,last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + '.'+ last + '@company.com'        
#         Employee.num_of_emps += 1
    
#     def fullname(self):
#         return '{} {}'.format(self.first, self.last) 
    
#     def apply_raise(self):
#         print(f'self.raise_amt = {self.raise_amt}')
#         print(f'Employee.raise_amt = {Employee.raise_amt}')         
#         self.pay = int(self.pay * self.raise_amt)

#     @classmethod
#     def set_raise_amt(cls, amount):
#         cls.raise_amt = amount    


# emp_1 = Employee('Corey','Schafer', 5000)
# emp_2 = Employee('Test','User', 6000)

# Employee.set_raise_amt(1.05)
# # emp_1.set_raise_amt(1.02)

# print(Employee.raise_amt)
# print(emp_1.raise_amt)
# print(emp_2.raise_amt)



# #////////////////////////////////////////
# class Employee:
#     num_of_emps = 0
#     raise_amt = 1.04  
      
#     def __init__(self,first,last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + '.'+ last + '@company.com'        
#         Employee.num_of_emps +=1
    
#     def fullname(self):
#         return '{} {}'.format(self.first, self.last) 
    
#     def apply_raise(self):        
#         self.pay = int(self.pay * self.raise_amount)

#     @classmethod
#     def set_raise_amt(cls, amount):
#         cls.raise_amt = amount

#     @classmethod
#     def from_string(cls, emp_str):
#         # print(emp_str)        
#         first, last, pay = emp_str.split('-')        
#         # print(first, last, pay)
#         print(cls(first, last, pay))        
#         return cls(first, last, pay)    
     


# emp_1 = Employee('Elyor','Dusnazarob', 5000)
# emp_2 = Employee('Test','User', 6000)

# emp_str_1 = 'John-Doe-70000'
# emp_str_2 = 'Steve-Smiths-30000'
# emp_str_3 = 'Jane-Doe-90000'


# new_emp_1 = Employee.from_string(emp_str_1)
# # new_emp_2 = Employee.from_string(emp_str_2)
# # new_emp_3 = Employee.from_string(emp_str_3)


# # print(new_emp_1.email)
# # print(new_emp_1.pay)


#////////////////////////////////////////
# class Employee:
#     num_of_emps = 0
#     raise_amt = 1.04  
      
#     def __init__(self,first,last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + '.'+ last + '@company.com'        
#         Employee.num_of_emps +=1
    
#     def fullname(self):
#         return '{} {}'.format(self.first, self.last) 
    
#     def apply_raise(self):        
#         self.pay = int(self.pay * self.raise_amount)                     
           
     
#     @staticmethod
#     def is_workday(day):
#         if day.weekday() == 5 or day.weekday() == 6:
#             return False
#         return True
                  
# emp_1 = Employee('Corey','Schafer', 5000)
# emp_2 = Employee('Test','User', 6000)

# import datetime
# my_date = datetime.date(2023, 4, 8)

# print(Employee.is_workday(my_date))






