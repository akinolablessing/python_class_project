class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self.name
    @name.setter
    def name(self, value):
        self.name = value
    @property
    def age(self):
        return self.age
    @age.setter
    def age(self, value):
        self.age = value
student = Student("John", 22)
print(student)

