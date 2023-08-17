class Parent():
    def property(self):
        print("Land, cash., jewel")
    def marriage(self):
        print("arrange marriage")
class Child(Parent):
    def marriage(self):
        print("Love marriage")
c=Child()
c.property()
c.marriage()