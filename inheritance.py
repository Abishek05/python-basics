class Person:

    def __init__(self, first, last):
        self.firstName = first
        self.lastName = last

    def get_fullname(self):
        return self.firstName + ' ' + self.lastName


class Employee(Person):

    def __init__(self, first, last, employeenumber):
        Person.__init__(self, first, last)
        self.employeeNumber = employeenumber

    def get_employee(self):
        return Person.get_fullname(self) + ' ' + self.employeeNumber


firstPerson = Person('Jane', 'Doe')
print(firstPerson.get_fullname())
print(firstPerson.firstName)
print(firstPerson.lastName)

firstEmployee = Employee('Jack', 'Ma', '1')
print(firstEmployee.get_fullname())
print(firstEmployee.firstName)
print(firstEmployee.lastName)
print(firstEmployee.employeeNumber)
print(firstEmployee.get_employee())
