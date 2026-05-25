# Getting the inputs
time = input("Enter Shift Hours:")
time2 = input("Enter Overtime Hours:")
pay = input("Enter hourly rate:")
hrs = float(time)
money = float(pay)
time1 = float(time2)

#Calculating Pay for first 40 hours
a = hrs * money

# Calculating Overtime Pay
b = money * 1.5
c = time1 * b

#Calculating total pay
x = a + c
print(x)
