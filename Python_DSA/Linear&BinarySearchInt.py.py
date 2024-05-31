# Linear Search in Python

n = int(input("Enter the length of array: "))
flag = 0
print("Enter Numbers: ")
arr = []
for i in range(n):
  arr.insert(i, int(input()))
print("Enter the Number to Search: ")
num = int(input())
for i in range(n):
  if num==arr[i]:
    flag = 1
    break
if flag == 0:
  print("data not found")
else:
  print("\nNumber Found at Index Number: ")
  print(i)

  



#Binary Search in Python
n = int(input("Enter the length of array: "))
print("Enter Numbers: ")
arr = []
for i in range(n):
  arr.insert(i, int(input()))
print("Enter the Number to Search: ")
num = int(input())
low = 0
high = n
flag = 0
for i in range(n):
  mid = (low  + high)// 2;
  if num==arr[i]:
    flag = 1
    break
  elif num > arr[mid]:
      low = mid;
  elif  num < arr[mid]:
      high = mid;
if(flag == 0):
    print("data not found")   
else:
    print("data found at ", mid)        



        
