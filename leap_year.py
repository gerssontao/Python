print("Welcome to my app to calc Leap year or common year!!!")
year = int(input("Enter a year: "))

#
# Put your code here.
if year>=1582:
    if year%4!=0:
        print("The year", year, "is common year")
    elif year%100!=0:
        print("The year", year, "is leap year")
    elif year%400!=0:
        print("The year", year, "is common year")
    else:
        print("The year", year, "is leap year")
else:
    print("Not within the Gregorian calendar period")
    
