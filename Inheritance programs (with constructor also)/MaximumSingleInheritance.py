class Numbers:
    def ReadData(self):
        self.num1 = int(input("Enter number1 = "))
        self.num2 = int(input("Enter number2 = "))
        self.num3 = int(input("Enter number3 = "))


class MaximumSingleInheritance(Numbers):
    def cal_display(self):
        if (self.num1 > self.num2) and (self.num1 > self.num3):
            maximum = self.num1
        elif (self.num2 > self.num1) and (self.num2 > self.num3):
            maximum = self.num2
        else:
            maximum = self.num3
        print("Maximum of 3 numbers is  = ",maximum)

#main code
m = MaximumSingleInheritance()
m.ReadData()
m.cal_display()
