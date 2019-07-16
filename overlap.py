# a function overlapping() that takes two lists and returns True if they have at least one member in common, False otherwise.

l1=[1,2,3,4,5]
l2=[6,7,8]
def overlap(a,b):
    a=set(l1)
    b=set(l2)
    if (a&b):
        return True
    else:
        return False
    
print(overlap(l1,l2))

