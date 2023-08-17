class Parent():
    def random(self):
        print("I am parent calss")
    def income(self):
        print("This is my income")
class  Child(Parent):
    def Childfun(self):
        print("I am child")

child1= Child()
child1=Child.income()
child1=Child.random()
child1=Child.Childfun()