class Student():
    cname = "texas"
    def __init__(self,name, roll):
        self.__name = name   #private varaible
        self.roll=roll
    def disPLy(self):
        print(self.name)
student1 = Student("Ram",50)
print(student1.namne)