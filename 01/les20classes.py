my_student = {
    'name': 'Rolf Smith',
    'grades': [70, 80, 90, 99],
    'average': 85  # Someting that calc avg 1
}


# Dict does not allow func use it's data inside it

def average_grade(student):
    return sum(student['grades']) / len(student['grades'])


print(average_grade(my_student))


class Student:

    def __init__(self, new_name, new_grades):  # dunder init
        """ property of self """
        self.name = new_name
        self.grades = new_grades

    def average(self):
        return sum(self.grades) / len(self.grades)


student_one = Student('Rolf Smith', [70, 80, 90, 99])

# print(student_one.name, student_one.average())
print(Student.average(student_one))

# Everything in python is an object
