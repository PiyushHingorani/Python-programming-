#bubble sort in python

n = int(input("Enter the length of array: "))
print("Enter Numbers: ")
arr = []
for i in range(n):
  arr.insert(i, int(input()))
count = 0
swap = int(input())
for i in range(n):
    for j in range(n-1):
        count = count + 1
        if arr[j] > arr[j+1]:
            swap = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = swap
for i in range(n):
    print("Sorted list is: :", arr[i])
print("Data Sorted counts are: ", count)    


