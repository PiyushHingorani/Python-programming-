# Linear Search of character in Python

n = int(input("Enter the length of array: "))
flag = 0
print("Enter characters: ")
arr = []
for i in range(n):
  arr.insert(i, str(input()))
print("Enter the character to Search: ")
s1 = str(input())
for i in range(n):
  if s1==arr[i]:
    flag = 1
    break
if flag == 0:
  print("data not found")
else:
  print("\ncharacter Found at Index Number: ")
  print(i)


#Binary Search of character in Python
n = int(input("Enter the length of array: "))
flag = 0
print("Enter characters: ")
arr = []
for i in range(n):
  arr.insert(i, str(input()))
print("Enter the character to Search: ")
s1 = str(input())
low = 0
high = n
flag = 0
for i in range(n):
  mid = (low  + high)// 2;
  if s1==arr[i]:
    print("data found at ", mid)        
    flag = 1
    break
  elif s1 > arr[mid]:
      low = mid;
  elif  s1 < arr[mid]:
      high = mid;
if(flag == 0):
    print("data not found")   

    
