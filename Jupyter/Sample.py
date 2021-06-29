#!/usr/bin/env python
# coding: utf-8

# In[22]:


class Employee:
#     empId
#     empName
#     jobTitle
    
    def __init__(self, empId,empName, jobTitle,salary):
        self.empId = empId
        self.empName = empName
        self.jobTitle = jobTitle
        self.salary = salary
    
# newEmp = Employee(100,'Arun', 'TL')

for i in range(1,10):
    globals()['newEmp%s' % i] = Employee(100+i,'Arun'+str(i),'TL',1000+i)

salary = []
for i in range(1,10):
    salary.append(globals()['newEmp%s' %i].salary)
    print("Employee Id:",globals()['newEmp%s' % i].empId,"Employee Name:",globals()['newEmp%s' % i].empName,
      "Employee Job Title:",globals()['newEmp%s' % i].jobTitle, globals()['newEmp%s' %i].salary)
    
print(max(salary))
print(min(salary))


# In[ ]:




