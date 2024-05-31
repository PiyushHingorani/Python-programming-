/******************************************************************************

Welcome to GDB Online.
  GDB online is an online compiler and debugger tool for C, C++, Python, PHP, Ruby, 
  C#, OCaml, VB, Perl, Swift, Prolog, Javascript, Pascal, COBOL, HTML, CSS, JS
  Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <iostream>
#include <conio.h>
using namespace std;

class EmployeeDetails
{
    protected:
               char name[20];
               int empid;
    public:
            void readData()
            {
                cout<<"\nEnter Name: "<<endl;    
                cin>>name;
                cout<<"\nEnter Employee ID: "<<endl;    
                cin>>empid; 
            }
};
class BasicSalary: public EmployeeDetails 
{
    protected:
            int bs;
    public:
            void readsalary()
            {
              cout<<"\nEnter basic salary: "<<endl;    
              cin>>bs;   
            }
};
class Overtime
{
    protected:
            double overtime;
            int hrs;
    public:
            void readhours()
            {
                cout<<"\nEnter the number of hours worked: "<<endl;
                cin>>hrs;
            }
            void cal_overtime(int bs)
            {
                overtime = hrs * bs * 1.20;
            }
};
class NetSalary: public BasicSalary, public Overtime
{
    private:
            double da, hra, ta, cla, netsal;
    public:
            void cal_display()
            {
                da = 1.54 * bs;
                hra = 0.20 * bs;
                cla = 0.05 * bs;
                ta = 2.04 * bs;
                netsal = bs + da + hra + cla + ta + overtime; 
                cout<<"\nEmployee name: "<<name<<"\n";
                cout<<"\nEmployee ID: "<<empid<<"\n";
                cout<<"\nBasic Salary: "<<bs<<"\n";
                cout<<"\nOvertime: "<<overtime<<"\n";
                cout<<"\nDA: "<<da<<"\n";
                cout<<"\nHRA: "<<hra<<"\n";
                cout<<"\nCLA: "<<cla<<"\n";
                cout<<"\nTA: "<<ta<<"\n";
                cout<<"\nNet Salary is: "<<netsal<<"\n";
            }
};
int main()
{
    int bs;
    NetSalary ns;
    ns.readData();
    ns.readsalary();
    ns.readhours();
    ns.cal_overtime(bs);
    ns.cal_display();
    getch();
}