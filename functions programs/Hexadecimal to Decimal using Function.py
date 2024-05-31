def HexToDec(h):
    return int(h, 16)

print("Enter Hexadecimal Number: ", end="")
hnum = input()

dnum = HexToDec(hnum)
print("\nEquivalent Decimal Value =", dnum)
