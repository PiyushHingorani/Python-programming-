def OctToHex(o):
    return hex(int(o, 8))

print("Enter Octal Number: ", end="")
onum = input()

hnum = OctToHex(onum)
print("\nEquivalent Hexadecimal Value =", hnum[2:].upper())
