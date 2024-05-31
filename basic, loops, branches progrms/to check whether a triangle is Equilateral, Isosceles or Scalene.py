a, b, c = map(int,(input("Enter the three sides of triangle: \n").split()))

    
if(a==b or b==c or c==a):
   {
     print("\nTriangle is isoceles")
   }
elif(a==b and b==c):
   {
      print("\nTriangle is equilateral")
   }  
else:
   {
      print("\nTriangle is scalene")
   }
