print("Enter Hexadecimal Number: ", end="")
hnum = input()

onum = int(hnum, 16)
onum = oct(onum)
print("\nEquivalent Octal Value = ", onum)


##using functions
def HexToOct(h):
    return oct(int(h, 16))

print("Enter Hexadecimal Number: ", end="")
hnum = input()

onum = HexToOct(hnum)
print("\nEquivalent Octal Value = ", onum[2:])
