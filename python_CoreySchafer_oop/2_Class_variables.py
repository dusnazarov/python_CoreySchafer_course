# #///////////////// class variables  ///////////////////////
# class Pay:
#     raise_amount = 1.1
        
#     def __init__(self, pay):        
#         self.pay = pay      
    
  
#     def apply_raise(self):
#         print(f'Pay.raise_amount = {Pay.raise_amount}')
#         print(f'self.raise_amount = {self.raise_amount}')         
#         self.pay = int(self.pay * Pay.raise_amount)

   
       

# p1 = Pay(1000)
# print(p1.__dict__)
# p1.apply_raise()
# print(p1.__dict__)
# print(Pay.__dict__)

# print('//////////  p1.raise_amount = 1.2 - change object variable //////////////////')

# p1 = Pay(1000)
# print(p1.__dict__)
# p1.raise_amount = 1.2
# p1.apply_raise()
# print(p1.__dict__)
# print(Pay.__dict__)

# print('//////////  Pay.raise_amount = 1.2  -- change class variable  //////////////////')

# p1 = Pay(1000)
# print(p1.__dict__)
# Pay.raise_amount = 1.2
# p1.apply_raise()
# print(p1.__dict__)
# print(Pay.__dict__)


# # #///////////////// class variables  ///////////////////////
# class Pay:
#     raise_amt = 0
        
#     def __init__(self, pay):        
#         self.pay = pay      
    
  
#     def apply_raise(self):
#         print(f'Pay.raise_amt = {Pay.raise_amt}')
#         print(f'self.raise_amt = {self.raise_amt}')         
#         self.pay = int(self.pay * Pay.raise_amt)
    
#     # @classmethod
#     # def set_raise_amt(cls, amount):
#     #     cls.raise_amt = amount    

   
       


# Pay.raise_amt = 1.1
# print(Pay.raise_amt)

# p1 = Pay(1000)
# # p1.raise_amt = 1.2
# print(p1.raise_amt)

# p2 = Pay(2000)
# # p2.raise_amt = 1.3
# print(p2.raise_amt)


#////////////////////////////////////////
# class Employee:
#     num_of_emps = 0
#     raise_amount = 1.04  
      
#     def __init__(self,first,last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + '.'+ last + '@company.com'        
#         Employee.num_of_emps += 1
    
#     def fullname(self):
#         return '{} {}'.format(self.first, self.last) 
    
#     def apply_raise(self):        
#         self.pay = int(self.pay * self.raise_amount)
       
# print(Employee.num_of_emps)

# emp_1 = Employee('Corey','Schafer', 5000)
# emp_2 = Employee('Test','User', 6000)

# print(Employee.num_of_emps)
