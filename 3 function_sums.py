# Write three functions that compute the sum of the numbers in a list: using a for-loop, a while-loop and recursion.
 
 # For loop
li=[1,2,3,4,5]
t=0
for elem in li:
    t=t+elem
print(t)


# while loop

li=[1,2,3,4,5]
t=0
index=0
while index< len(li):
    t+=li[index]
    index+=1 
print(t)


#recursion

def sums(li):
    if len(li)==1:
        return li[0]
    else:
        return li[0]+sums(li[1:])
print(sums([1,2,3,4,5,6]))
