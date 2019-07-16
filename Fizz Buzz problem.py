# check whether the number is divisible by three or seven or both

a=int(input('enter no '))
if (a%3==0) & (a%7==0):
    print('both')
elif (a%3==0):
    print('by 3')
else:
    print('by 7')
