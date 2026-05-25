score = input("Enter your score:")
x = float(score)

if x < 0.0 :
    print('These marks are not eligible for obtaining a grade. Study harder for the next test!')
elif x < 0.6 :
    print('F')
elif 0.6 <= x < 0.7  :
    print('D')
elif 0.7 <= x < 0.8 :
    print('C')
elif 0.8 <= x < 0.9 :
    print('B')
elif 0.9 <= x < 1.0 :
    print('A')
else : 
    print('Please enter marks within the range.')

