# bubble sort algorithm using python

def bubble(li):
    for no in range(len(li)-1,0,-1):
        for i in range(no):
            if li[i]>li[i+1]:
                temp=li[i]
                li[i]=li[i+1]
                li[i+1]=temp
li=[1,80,40,5,4,63,45,7,0]
bubble(li)
print(li)
            
            
