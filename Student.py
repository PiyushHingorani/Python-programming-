class Student:
    def __init__(self, a, b):
        self.x = a
        self.y = b
    def display(self):
        print(self.x)
        print(self.y)

#main code
st = Student(10, 20)
st.display()

class Student:
     def ReadData(self, a, b):
         self.x = a
         self.y = b
     def display(self):
         print(self.x)
         print(self.y)

#main code
st = Student()
st.ReadData(10, 20)
st.display()
