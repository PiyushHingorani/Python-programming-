Number = int(input("Please Enter any Number: "))
Rev = 0
while(Number > 0):
    Reminder = Number % 10
    Rev =   Rev * 10 + Reminder
    Number = Number //10

print("\nReverse of the digits of Given Number = ", Rev)

