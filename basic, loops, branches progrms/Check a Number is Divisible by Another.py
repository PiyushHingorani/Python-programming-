print("Enter a Number (Numerator): ")
numn = int(input())
print("Enter a Number (denominator): ")
numd = int(input())

if numn%numd==0:
  print("\n" +str(numn)+ " is divisible by " +str(numd))
else:
  print("\n" +str(numn)+ " is not divisible by " +str(numd))

##Divisibility Test with Multiple Numbers


print("Enter the Size: ", end="")
tot = int(input())
print("Enter " +str(tot)+ " Numbers: ", end="")
nums = []
for i in range(tot):
  nums.append(int(input()))

print("\nEnter a Number to Apply Divisibility Test: ", end="")
val = int(input())

res = []
for i in range(tot):
  if nums[i]%val==0:
    res.append(nums[i])

reslen = len(res)
if reslen>0:
  if reslen>1:
    print("\nThere are " +str(reslen)+ " numbers divisible by " +str(val))
    for i in range(reslen):
      print(res[i], end=" ")
    print()
  else:
    print("\nThere is only 1 number divisible by " +str(val))
    print(res[0])
else:
  print("\nThere is no any number divisible by " +str(val))
