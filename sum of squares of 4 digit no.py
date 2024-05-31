Number = int(input("Please Enter any Number: "))
Sum = 0
while(Number > 0):
    Reminder = Number % 10
    Sum =   Sum + Reminder * Reminder
    Number = Number //10

print("\nSum of Squares of the digits of Given Number = ", Sum)


