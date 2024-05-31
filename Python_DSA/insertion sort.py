#insertion sort in python

n = int(input("Enter the length of array: "))
print("Enter " +str(n)+" Numbers: ")
arr = []
for i in range(n):
  arr.insert(i, int(input()))
count = 0
for i in range(1, n):
    count = count + 1
    current = arr[i]
    j = i-1
    # Compare key with each element on the left of it until an element smaller than it is found
    # For descending order, change key<array[j] to key>array[j].        
    while j>=0 and arr[j] > current:
        arr[j+1] = arr[j]
        j=j-1
    arr[j+1] = current         # Place key at after the element just smaller than it.
for i in range(n):
    print("Sorted list is: :", arr[i])
print("Data Sorted counts are: ", count)    
    

#alternate code

arr = []
print(end="Enter the Size: ")
arrSize = int(input())
print("Enter " +str(arrSize)+ " Elements: ")
for i in range(arrSize):
  arr.append(int(input()))

for i in range(1, arrSize):
  elem = arr[i]
  if elem<arr[i-1]:
    for j in range(i+1):
      if elem<arr[j]:
        index = j
        for k in range(i, j, -1):
          arr[k] = arr[k-1]
        break
  else:
    continue
  arr[index] = elem

print("\nThe New (Sorted) List is: ")
for i in range(arrSize):
  print(end=str(arr[i]) + " ")

print()
