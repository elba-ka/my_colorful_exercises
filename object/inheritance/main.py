class Person:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def welcome(self):
        return "welcome", self.fname, self.lname

    # @property
    # def name(self):
    #     return print(self.fname, self.lname)

class Student(Person):

    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduationyear = 2020






#
# x = Person("el", "ba")
# print(x.name)

x = Person("el", "ba")
x = Student("el", "ba")
print(x.fname, x.lname, x.graduationyear, x.welcome())



