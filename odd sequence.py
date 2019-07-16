# Take a list as input and returns the elements on odd positions in a list.
   
li=[2,58,3,8,6,5,5,86,78]
    print(li[::2])
    
    
    
# a program which takes a number as input from user (n) and prints the sum of only multiples of three or five from 1-n, e.g. 3+5+6+9+10+12+15 for n=17

n=int(input('enter no '))
t=0
for elem in range (1,n+1):
    if(elem%3==0) or (elem%5==0):
        t=t+elem
print(t)
    
