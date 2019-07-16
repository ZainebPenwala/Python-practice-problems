# sum of all elements in a list

li=[1,2,3,4,5,6,7,8,9]
t=0
for elem in li:
    t=t+elem
print(t)



# sum of all individual digits from a list of integer

li=[11,12,13,14,15]
t=0
for elem in li:
    for i in str(elem):
        t+= int(i)
print(t)
