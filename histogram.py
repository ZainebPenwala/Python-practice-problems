# a histogram() that takes a list of integers and prints a histogram to the screen. For example,histogram([4, 9, 7]) should print the following:
**** = 4 stars

def histogram(s):
    for n in s:
        output=''
        times=n 
        while (times>0):
            output+='*'
            times=times-1
        print(output)
histogram([1,2,3])

     
