def checkArmstrongNum(x):
    noOfDigit = 0
    res = 0
    temp = x
    while x>0:
        x = int(x/10)
        noOfDigit = noOfDigit + 1
    x = temp
    while x>0:
        rem = x%10
        pow = 1
        i = 0
        while i<noOfDigit:
            pow = pow * rem
            i = i + 1
        res = res + pow
        x = int(x/10)

    if res==temp:
        return 1
    else:
        return 0

print("Enter the Number: ", end="")
num = int(input())

chk = checkArmstrongNum(num)
if chk==1:
    print(num, "is an Armstrong Number")
else:
    print(num, "is not an Armstrong Number")
