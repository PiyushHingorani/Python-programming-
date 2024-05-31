def BinToDec(b):
    return int(b, 2)

print("Enter the Binary Number: ", end="")
bnum = input()

dnum = BinToDec(bnum)
print("\nEquivalent Decimal Value = ", dnum)
