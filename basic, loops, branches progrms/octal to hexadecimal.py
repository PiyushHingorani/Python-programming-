##Octal to Hexadecimal using String and while Loop
print("Enter the Octal Number: ", end="")
onum = int(input())

chk = i = dnum = 0
while onum!=0:
    rem = onum % 10
    if rem>7:
        chk = 1
        break
    dnum = dnum + (rem * (8 ** i))
    i = i+1
    onum = int(onum / 10)

if chk == 0:
    hnum = ""
    while dnum != 0:
        rem = dnum % 16
        if rem < 10:
            rem = rem + 48
        else:
            rem = rem + 55
        rem = chr(rem)
        hnum = hnum + rem
        dnum = int(dnum / 16)
    hnum = hnum[::-1]
    print("\nEquivalent Hexadecimal Value =", hnum)

else:
    print("\nInvalid Input!")


##Octal to Hexadecimal using int() and hex()
print("Enter Octal Number: ", end="")
onum = input()

dnum = int(onum, 8)
hnum = hex(dnum)
print("\nEquivalent Hexadecimal Value =", hnum)
