x = int(input("Enter the coordinate x: "))
y = int(input("Enter the coordinate y: "))             

if x > 0 and y > 0:
	 {
	     print("\n It lies in first quadrant", x, y)
	 }    
elif x < 0 and y > 0:
	 {
	     print("\n(It lies in second quadrant", x, y)
	 }    
elif x < 0 and y < 0:
	 {
	     print("\n(It lies in third quadrant", x, y)
	 }    
elif x > 0 and y < 0:
	 {
	     print("\nIt lies in fourth quadrant", x, y)
	 }    
else:
	 {
	     print("\n(It lies at origin", x, y)
	 } 
	 
