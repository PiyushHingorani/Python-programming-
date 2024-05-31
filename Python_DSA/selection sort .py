#selection sort in python

n = int(input("Enter the length of array: "))
print("Enter Numbers: ")
arr = []
for i in range(0, n):
  arr.append(int(input()))
count = 0
swap = int(input())
min_index = int(input())
for i in range(0, n-1):
    min_index = i
    for j in range(i+1, n):
        count = count + 1
        if arr[j] < arr[min_index]:
            min_index = j
    swap = arr[i]
    arr[i] = arr[min_index]
    arr[min_index] = swap     
for i in range(n):
    print("Sorted list is: :", arr[i])
print("Data Sorted counts are: ", count)    


