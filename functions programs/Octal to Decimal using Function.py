def OctToDec(o):
    return int(o, 8)

print("Enter the Octal Number: ", end="")
onum = input()

dnum = OctToDec(onum)
print("\nEquivalent Decimal Value =", dnum)
