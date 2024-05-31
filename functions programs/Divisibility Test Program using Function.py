def divTest(x, y):
  if x%y==0:
    return 1

print("Enter the Size: ", end="")
tot = int(input())

print("Enter " +str(tot)+ " Numbers: ", end="")
nums = []
for i in range(tot):
  nums.append(int(input()))

print("\nEnter a Number to Apply Divisibility Test: ", end="")
val = int(input())

for i in range(tot):
  if divTest(nums[i], val) == 1:
    print(nums[i])
