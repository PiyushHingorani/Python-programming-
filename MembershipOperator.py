str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

if str2 in str1:
    print(str2+'found in the first string')
else:
    print(str2+'not found in the first string')


if str2 not in str1:
    print(str2+'not found in the first string')
else:
    print(str2+'found in the first string')
