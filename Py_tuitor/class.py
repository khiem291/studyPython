'''
Created on Oct 10, 2014

@author: khiemtd
'''
class Employee:
   'Common base class for all employees' 
   __count = 1
   empCount = 0 
 
   def __init__(self, name, salary): 
      self.name = name 
      self.salary = salary 
      Employee.empCount += 1 
    
   def displayCount(self): 
     print "Total Employee %d" % Employee.empCount 
 
   def displayEmployee(self): 
      print "Name : ", self.name,  ", Salary: ", self.salary 
 
"This would create first object of Employee class" 
emp1 = Employee("Zara", 2000) 
"This would create second object of Employee class" 
emp2 = Employee("Manni", 5000) 
emp1.displayEmployee() 
emp2.displayEmployee() 
print "Total Employee %d" % Employee.empCount 

# add attribute, get, del
setattr(Employee, 'age', 7)
print getattr(Employee, 'age')
delattr(Employee, 'age')

# Built in
print Employee.__doc__
print Employee.__name__
print Employee.__module__

#del obj, sub, isinstance
print id(emp1), id(emp2)
del emp2; #print id(emp2)
class subnho(Employee):
    pass
print issubclass(subnho, Employee)
print isinstance(emp1, Employee)
print emp1._Employee__count #print emp1.__count
