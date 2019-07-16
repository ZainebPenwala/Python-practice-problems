# a function which takes as input two lists and returns a new list with elements of both those two lists.

l1=[1,3,5,7,9]
l2=[2,4,6,8,10]
l3=[]
def add (a,b):
    a=set(l1)
    b=set(l2)
    l3=a.union(b)
    return l3
print(list(add(l1,l2)))
