print("Enter a Number: ", end="")
n = int(input())

p = 0
for i in range(2, n):
    if n%i==0:
        p = 1
        break

if p==0:
    print("\n" +str(n)+ " is a Prime Number")
else:
    print("\n" +str(n)+ " is not a Prime Number")



## while loop
print("Enter a Number: ", end="")
n = int(input())

p = 0
i = 2
while i<n:
    if n%i==0:
        p = 1
        break
    i = i+1

if p==0:
    print("\n" +str(n)+ " is a Prime Number")
else:
    print("\n" +str(n)+ " is not a Prime Number")
