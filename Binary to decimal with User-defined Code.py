print("Enter the Binary Number: ")
binarynum = int(input())

octaldigit = 0
octalnum = []
i = 0
mul = 1
chk = 1
while binarynum!=0:
    rem = binarynum % 10
    octaldigit = octaldigit + (rem * mul)
    if chk%3==0:
        octalnum.insert(i, octaldigit)
        mul = 1
        octaldigit = 0
        chk = 1
        i = i+1
    else:
        mul = mul*2
        chk = chk+1
    binarynum = int(binarynum / 10)

if chk!=1:
    octalnum.insert(i, octaldigit)

print("\nEquivalent Octal Value = ", end="")
while i>=0:
    print(str(octalnum[i]), end="")
    i = i-1
print()

##Binary to Octal using int() and oct()
print("Enter a Binary Number: ", end="")
bnum = input()

onum = int(bnum, 2)
onum = oct(onum)

print("\nEquivalent Octal Value = ", onum)
