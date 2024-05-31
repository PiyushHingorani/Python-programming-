# Linear Search of String in Python

n = int(input("Enter the length of array: "))
flag = 0
print("Enter string names: ")
arr = []
for i in range(n):
  arr.insert(i, str(input()))
print("Enter the string name to Search: ")
s1 = str(input())
for i in range(n):
  if s1==arr[i]:
    flag = 1
    break
if flag == 0:
  print("data not found")
else:
  print("\nString name Found at Index Number: ")
  print(i)



        

