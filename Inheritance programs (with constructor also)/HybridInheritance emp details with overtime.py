class EmployeeDetails:
    def readDetails(self):
        self.name = str(input("Enter employee name= "))
        self.empid = int(input("Enter employee id= "))

class BasicSalary(EmployeeDetails):
    def readsalary(self):
        self.bs = int(input("Enter basic salary= "))


class OverTime():
    def readhours(self):
        self.hrs = int(input("Enter Number of hours= "))
    def cal_overtime(self):
        self.overtime = self.hrs * 0.20 * self.bs
        
class NetSalary(OverTime, BasicSalary):
    def cal_display(self):
        self.da = 1.54 * self.bs
        self.hra = 0.20 * self.bs
        self.cla = 0.05 * self.bs
        self.ta = 2.04 * self.bs
        self.netsal = self.bs + self.da + self.hra + self.cla + self.ta + self.overtime    
        print("\nEmployee name: ",self.name)
        print("\nEmployee ID: ",self.empid)
        print("\nBasic Salary: ",self.bs)
        print("\nOvertime: ",self.overtime)
        print("\nDA: ",self.da)
        print("\nHRA: ",self.hra)
        print("\nCLA: ",self.cla)
        print("\nTA: ",self.ta)
        print("\nNet Salary is: ",self.netsal)


##main code
ns = NetSalary()
ns.readDetails()
ns.readsalary()
ns.readhours()
ns.cal_overtime()
ns.cal_display()

        
    
       
        
