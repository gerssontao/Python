# we will store the current largest number here
largestNumber = -999999999
counter=0
while True:
    # input the first value
    number = int(input("Enter a number or type -1 to stop: "))
  
    # is number larger than largest_number?
    if number == -1 :
        break
    counter +=1
    if number>largestNumber:
        # yes, update largest_number
        largest_number = number
if counter !=0:
    # print the largest number
    print("The largest number is:", largest_number)
else:
    print("you haven't entered any number")

largestNumber = -99999999
counter = 0

number = int(input("Enter a number or type -1 to end program: "))

while number != -1:
    if number == -1:
        continue
    counter += 1

    if number > largestNumber:
        largestNumber = number
    number = int(input("Enter a number or type -1 to end program: "))

if counter:
    print("The largest number is", largestNumber)
else:
    print("You haven't entered any number.")