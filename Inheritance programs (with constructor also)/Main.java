/******************************************************************************

Welcome to GDB Online.
  GDB online is an online compiler and debugger tool for C, C++, Python, PHP, Ruby, 
  C#, OCaml, VB, Perl, Swift, Prolog, Javascript, Pascal, COBOL, HTML, CSS, JS
  Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
import java.util.*;
abstract class Employee
{
    String name; 
    int empid;
    int basicsal;
    
    abstract void getData(String nm, int eid, int bs);
}
class Netsalary extends Employee
{
    void getData(String nm, int eid, int bs)
	{
	    name = nm;
	    empid = eid;
	    basicsal = bs;
	}
    double da, hra, cla, ta, netsal;
    void cal_display()
	{
	    da = 1.54 * basicsal;
        hra = 0.20 * basicsal;
        cla = 0.05 * basicsal;
        ta = 2.04 * basicsal;
        netsal = basicsal + da + hra + cla + ta; 
            
        System.out.println("Employee name: "+name);
        System.out.println("Employee ID: "+empid);
        System.out.println("Basic Salary: "+basicsal);
        System.out.println("DA: "+da);
        System.out.println("HRA: "+hra);
        System.out.println("CLA: "+cla);
        System.out.println("TA: "+ta);
        System.out.println("Net Salary is: "+netsal);
	}
	
}
class Main
{
    static String name;
    static int empid, basicsal;
    public static void main(String[] args)
    {
        Scanner scn = new Scanner(System.in);
        System.out.println("\n Enter the name =");
        String name = scn.nextLine();
        System.out.println("\n Enter the employee id =");
        empid = scn.nextInt();
        System.out.println("\n Enter the basic salary =");
        basicsal = scn.nextInt();
        Netsalary ns = new Netsalary();
        ns.getData(name, empid, basicsal);
        ns.cal_display();
    }    
}