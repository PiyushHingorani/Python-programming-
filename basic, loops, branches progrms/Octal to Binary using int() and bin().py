print("Enter Octal Number: ", end="")
onum = input()

bnum = int(onum, 8)
bnum = bin(bnum)

print("\nEquivalent Binary Value =", bnum)
