# Complete the following code according to the task in README.md.
# Don't change names of classes. Create names for the variables
# exactly the same as in the task.
class SchoolMember:
    name = ""
    age = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        return f'Name: {self.name}, Age: {self.age}'


class Teacher(SchoolMember):
    _salary = 0

    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self._salary = salary

    def show(self):
        return super().show() + ', Salary: ' + str(self._salary)



class Student(SchoolMember):
    _grades = 0

    def __init__(self, name, age, grades):
        super().__init__(name, age)
        self._grades = grades

    def show(self):
        return super().show() + ', Grades: ' + str(self._grades)



if __name__ == '__main__':
    persons = [Teacher("Mr.Snape", 40, 3000), Student("Harry", 16, 75)]

    for person in persons:
        print(person.show())
