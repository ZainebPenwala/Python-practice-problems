# a program that prints the next 20 leap years.

for a in range (2020,2041):
    if (a%4==0) or (a%400==0):
        print(a,'LEAP YEAR!!')
    else:
        print(a,'NOT A LEAP YEAR')
