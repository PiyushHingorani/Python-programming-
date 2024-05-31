num = int(input("Enter the number = "))

fact = 1
i = 1
 
while i <= num:
    fact = fact * i
    i = i + 1
 
print("factorial of ", num, " is ", fact)
