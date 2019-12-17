print("Welcome to my app to calc taxes!!!")
income = float(input("Enter the annual income: "))
tax_relief=556.02

if income<=85528:
    tax=(income*0.18)-tax_relief
elif income>85528:
    tax=14839.02 + ((income-85528)*0.32)
if tax<=0:
    tax=0

tax = round(tax, 0)
print("The tax is:", tax, "thalers")