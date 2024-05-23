class Employee:
    def __init__(self, first_name, last_name):
        self.fullname = first_name + ' ' + last_name
        self.email = (first_name + 'a' + last_name + '.sue@company').lower()
emp = Employee('John', 'Doe')
print(emp.fullname)
print(emp.email)
