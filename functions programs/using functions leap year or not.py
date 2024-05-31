def checkLeapOrNot(x):
    if y % 4 == 0 and y % 100 != 0:
        return 1
    elif y % 400 == 0:
        return 1

print("Enter the Year: ", end="")
y = int(input())

chk = checkLeapOrNot(y)
if chk==1:
    print("\n" +str(y)+ " is a Leap Year")
else:
    print("\n" +str(y)+ " is not a Leap Year")
