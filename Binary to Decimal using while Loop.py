print("Enter the Binary Number: ")
bnum = int(input())

dnum = 0
i = 1
while bnum!=0:
    rem = bnum%10
    dnum = dnum + (rem*i)
    i = i*2
    bnum = int(bnum/10)

print("\nEquivalent Decimal Value = ", dnum)

## binary to decimal using for loop
print("Enter the Binary Number: ", end="")
bnum = int(input())

dnum = 0
m = 1
blen = len(str(bnum))

for k in range(blen):
    rem = bnum%10
    dnum = dnum + (rem * m)
    m = m * 2
    bnum = int(bnum/10)

print("\nEquivalent Decimal Value = ", dnum)


##Binary to Decimal using int()
print("Enter the Binary Number: ", end="")
bnum = input()

dnum = int(bnum, 2)
print("\nEquivalent Decimal Value = ", dnum)
