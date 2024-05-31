print("Enter Two Numbers: ")
numOne = int(input())
numTwo = int(input())

if numOne>numTwo:
    lcm = numOne
else:
    lcm = numTwo

while True:
    if lcm%numOne==0 and lcm%numTwo==0:
        break
    else:
        lcm = lcm + 1

print("\nLCM =", lcm)


##GCD of 2 numbers

print("Enter Two Numbers: ", end="")
no = int(input())
nt = int(input())

if no>nt:
    hcf = no
else:
    hcf = nt

while True:
    if no%hcf==0 and nt%hcf==0:
        break
    else:
        hcf = hcf - 1

print("\nHCF (" + str(no) + ", " + str(nt) + ") = ", hcf)

##Find LCM and HCF using Formula

print("Enter Two Numbers: ", end="")
no = int(input())
nt = int(input())

a = no
b = nt
while b!=0:
    temp = b
    b = a%b
    a = temp

hcf = a
lcm = int((no*nt)/hcf)

print("\nLCM (" + str(no) + ", " + str(nt) + ") = ", lcm)
print("HCF (" + str(no) + ", " + str(nt) + ") = ", hcf)
