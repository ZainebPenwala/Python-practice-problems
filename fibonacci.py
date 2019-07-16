# print a list of first 50  fibonacci numbers

a=0
b=1
li=[a,b]
for _ in range(1,50):
    a,b=b,b+a 
    li.append(b)
print(li)
