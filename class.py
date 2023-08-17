class Student():
    cname = "texas"
    def __init__(self,name, roll):
        self.name = name   #instance variable
        self.roll=roll
    def display(self):
        print(self.name)
        print(self.roll)
    @staticmethod     #utility method
    def add(x, y):       #local veraible
        print(x + y)
    @classmethod            #class method
    def clzname(cls):
        print(cls.cname)


student1 = Student("Ram",50)
student2 = Student("Shyam",20)
Student.add(10,20)
student1.clzname()
# student1.display()
# student2.display()
# print(student1.__dict__)
# print(student2.__dict__)
# print(student2.cname)