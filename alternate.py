# Alternately print elements of 2 lists of equal length

l1=[1,2,3,4,5]
l2=['a','b','c','d','e']
def alt (a,b):
    final=[]
    for index in range(len(a)):
        final.append(a[index])
        final.append(b[index])
    return final 
print(alt(l1,l2))



# Altenately print elements of two lists of unequal length

l1=[1,2,3,4,5,6,7,8,9]
l2=['a','b','c']
def alt (a,b):
    longer= a if len(a)> len(b) else b 
    shorter= a if len(a)<len(b) else b 
    final=[]
    for index in range(len(shorter)):
        final.append(a[index])
        final.append(b[index])
    for elem in longer[index+1:]:
        final.append(elem)
    return final 
print(alt(l1,l2))
