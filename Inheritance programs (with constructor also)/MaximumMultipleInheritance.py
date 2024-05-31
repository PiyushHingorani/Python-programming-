class Number1:
    def Num1(self):
        self.num1 = int(input("Enter number1= "))

class Number2:
    def Num2(self):
        self.num2 = int(input("Enter number2= "))

class Number3:
    def Num3(self):
        self.num3 = int(input("Enter number3= "))

class MaximumMultipleInheritance(Number1, Number2, Number3):
    def cal_display(self):
        if (self.num1 > self.num2) and (self.num1 > self.num3):
            maximum = self.num1
        elif (self.num2 > self.num1) and (self.num2 > self.num3):
            maximum = self.num2
        else:
            maximum = self.num3
        print("Maximum of 3 numbers is  = ",maximum)

#main code
m = MaximumMultipleInheritance()
m.Num1()
m.Num2()
m.Num3()
m.cal_display()        

