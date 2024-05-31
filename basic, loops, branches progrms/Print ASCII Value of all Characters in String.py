print("Enter a String: ", end="")
text = input()

textlen = len(text)
for ch in text:
    asc = ord(ch)
    print(ch, "\t", asc)




##Modified Version of Previous Program

print("Enter a String: ", end="")
text = input()

text = "".join(dict.fromkeys(text))
textlen = len(text)
for ch in text:
    asc = ord(ch)
    print(ch, "\t", asc)
