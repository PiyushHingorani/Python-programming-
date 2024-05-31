def DecToBin(d):
    b = 0
    m = 1
    while d>0:
        b = b + ((d%2)*m)
        m = m*10
        d = int(d/2)
    return b

print("Enter Decimal Number: ", end="")
dnum = int(input())

bnum = DecToBin(dnum)
print("\nEquivalent Binary Value =", bnum)
