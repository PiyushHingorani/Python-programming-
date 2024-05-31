math = int(input("Enter marks of maths= "))
chem = int(input("Enter marks of chem= "))
phy = int(input("Enter marks of phy= "))

avg = (math + chem + phy)/3
    
if avg>90:
    {
        print("\nGrade is A")
    }
elif avg>70 and avg<=90:
    {
        print("\nGrade is B")
    }
elif avg>50 and avg<=70:
    {
        print("\nGrade is C")
    }
elif avg>40 and avg<=50:
    {
        print("\nGrade is D")
    }
else:
    {
        print("\nGrade is E")
    }
 
print("\nMarks of maths: ", math)
print("\nMarks of chemistry: ", chem)
print("\nMarks of physics: ", phy)
print("\nAverage of 3 subject marks: ", avg)

