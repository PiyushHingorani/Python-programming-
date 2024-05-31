import calendar

print("Enter Year: ")
yy = input()
print("\nEnter Month Number (1-12): ")
mm = input()

y = int(yy)
m = int(mm)
print("\n", calendar.month(y, m))


##exception handling
import calendar

print("Enter Year: ", end="")
try:
    yy = int(input())
    print("\nEnter Month Number (1-12): ", end="")
    try:
        mm = int(input())
        if mm>=1 and mm<=12:
            print("\n", calendar.month(yy, mm))
        else:
            print("\nInvalid Month Number!")
    except ValueError:
        print("\nInvalid Input!")
except ValueError:
    print("\nInvalid Input!")import calendar


##Display All Months (Whole Year) Calendar

import calendar

print("Enter Year: ", end="")
try:
    yy = int(input())
    print()
    mm = 1
    while mm<=12:
        print(calendar.month(yy, mm))
        mm = mm+1
except ValueError:
    print("\nInvalid Input!")
