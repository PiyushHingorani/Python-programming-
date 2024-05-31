class Area:
    def display(self):
        print("Area is = ",self.area)

class Circle(Area):
    def Radius(self):
        self.rd = int(input("Enter radius= "))
    def cal1(self):
        self.area = 3.14 * self.rd * self.rd
        
class Triangle(Area):
    def readtriangle(self):
        self.b = int(input("Enter base of triangle= "))
        self.h = int(input("Enter height of triangle= "))
    def cal2(self):
        self.area = 0.5 * self.b * self.h

class Rectangle(Area):
    def readrectangle(self):
        self.len = int(input("Enter length of rectangle= "))
        self.bdth = int(input("Enter breadth of rectangle= "))
    def cal3(self):
        self.area = self.len * self.bdth

##HierarchicalInheritance
#main code
cr = Circle()
cr.Radius()
cr.cal1()
cr.display()
t = Triangle()
t.readtriangle()
t.cal2()
t.display()
rt = Rectangle()
rt.readrectangle()
rt.cal3()
rt.display()
        
