def DecToOct(d):
    return oct(d)

print("Enter Decimal Number: ", end="")
dnum = int(input())

onum = DecToOct(dnum)
print("\nEquivalent Octal Value =", onum[2:])
