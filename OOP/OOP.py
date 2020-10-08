"""
    OOP in Python
    by Philipe Gouveia
    Oct 8th 2020
"""

#pass means "get out of here"

class Employee:
    #ATTRIBUTES: belong to class
    counter = 0
    #all instance attributes need to be declared inside the Constructor in python

    #CONSTRUCTOR: definition in a class __init__ with the self as attribute (self = this)
    #as they can be called out of an object scope, a constructor is a FUNCTION not a method
    def __init__(self, firstName = "Unkown", lastName = "Unkown", age = 0):
        #ATTRIBUTES: Instance level attribute
        self.fName = firstName
        self.lName = lastName
        self.age = age
        #incrementing the class attribute (such as statics)
        Employee.counter = Employee.counter + 1

    def getAge(self):
        return self.age
    def setAge(self, newAge):
        if (newAge > 18 and age < 60):
            self.age = newAge
        else: self.age = -1 


#OBJECT INSTANTIATION: instantiate an employee object
emp = Employee("Philipe", "Go", 35)
print(f"ID: {emp.counter} - {emp.fName} {emp.lName} - age: {emp.age}")
print(f"{type(emp)}")
#overloaded constructor
emp1 = Employee()
print(f"ID: {emp.counter} - {emp1.fName} {emp1.lName} - age: {emp1.age}")

#changing the object attributes
emp1.fName = "Lulu"
emp1.lName = "Prx"
emp1.age = 32
print(f"ID: {emp.counter} - {emp1.fName} {emp1.lName} - age: {emp1.age}")
