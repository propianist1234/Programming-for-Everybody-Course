hrs = float(input("Enter Working Hours: "))
rate = float(input("Enter Rate per Hour: "))

if hrs > 40 :
    paym = (hrs - 40) * rate * 1.5 + 40 * rate
elif hrs <= 40 :
    y = hrs * rate
else : 
    print('Please enter correct working hours.')

def computepay(hrs, rate) :
    if hrs > 40 :
        print('Pay', paym)
    else :
        print('Pay', y)
    return

computepay(hrs, rate)