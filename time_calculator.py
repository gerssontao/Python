hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# put your code here
print("The End time is: (24-hour format) " + str(int((hour+((mins+dura)/60)%24)%24))+str(":")+str((mins+dura)%60))
