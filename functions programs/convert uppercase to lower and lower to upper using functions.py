def UpToLow(u):
    return u.lower()

print("Enter the String: ", end="")
text = input()

text = UpToLow(text)
print("\nIts Lowercase:", text)

def LowToUp(l):
    return l.upper()

print("Enter the String: ", end="")
text = input()

text = LowToUp(text)
print("\nIts Uppercase:", text)
