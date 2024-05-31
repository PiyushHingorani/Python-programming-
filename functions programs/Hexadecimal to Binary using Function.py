print("Enter the Hexadecimal Number: ", end="")
hnum = input()

hnum = int(hnum, 16)
bnum = bin(hnum)
print("\nEquivalent Binary Value = ", bnum)

#using function

def HexToBin(h):
    return bin(int(h, 16))

print("Enter the Hexadecimal Number: ", end="")
hnum = input()

bnum = HexToBin(hnum)
print("\nEquivalent Binary Value = ", bnum[2:])
