def OctToBin(o):
    return bin(int(o, 8))

print("Enter Octal Number: ", end="")
onum = input()

bnum = OctToBin(onum)
print("\nEquivalent Binary Value =", bnum[2:])
