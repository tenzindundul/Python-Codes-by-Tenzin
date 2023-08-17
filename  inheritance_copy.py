class Parent(object):
    def __int__(self):
        print("I am parent")
    def display(self):
        print("I am the method from, parent class")
class Child(Parent):
    pass
child1=Child()
child1.display()