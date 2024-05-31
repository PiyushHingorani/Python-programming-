num1 = int(input("Enter the number1 = "))
num2 = int(input("Enter the number2 = "))
num3 = int(input("Enter the number3 = "))

if (num1 > num2) and (num1 > num3):
        maximum = num1
 
elif (num2 > num1) and (num2 > num3):
        maximum = num2
else:
        maximum = num3

print("Maximum of 3 numbers is  = ",maximum)        

