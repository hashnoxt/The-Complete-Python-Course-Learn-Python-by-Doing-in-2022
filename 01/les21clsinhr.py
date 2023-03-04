#Inheritance

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name,school)
        self.salary = salary

    @property # Now this function works as a value / Can't use with actions
    def weekly_salary(self):
        return self.salary * 37.5


rolf = WorkingStudent('Rolf', 'MIT', 12.5)
print(rolf.name, rolf.salary)
print(rolf.weekly_salary)
