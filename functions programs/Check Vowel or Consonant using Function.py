def checkVowel(x):
    if (c>='a' and c<='z') or (c>='A' and c<='Z'):
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        if c in vowels:
            return 1
        else:
            return 2

print(end="Enter a Character: ")
c = input()

size = len(c)
if size>1:
    print("\nInvalid Input!")
else:
    chk = checkVowel(c)
    if chk==1:
        print("\nVowel")
    elif chk==2:
        print("\nConsonant")
    else:
        print("\nNeither Vowel nor Consonant")
