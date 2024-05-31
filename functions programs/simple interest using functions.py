def simpleInterset(A, Y, R):
    # Calculate the simple interest
    SI = (A*Y*R)/100
    return SI


A = int(input("Enter the amount: "))
# Enter the number of years
Y = int(input("Enter the number of years: "))
# Enter the rate of interest
R = float(input("Enter the rate of interest: "))

print("The simple interest is:", simpleInterset(A, Y, R))
