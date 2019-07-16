# Implement merge sort algorithm using python.

def mergesort(li):
    if len(li)>1:
        mid=len(li)//2
        left=li[:	mid]
        right=li[mid:]
        
        mergesort(left)
        mergesort(right)
        
        i=0
        j=0
        k=0
        
        while i< len(left) and j< len (right):
            if left[i]<=right[j]:
                li[k]=left[i]
                i=i+1 
                k=k+1 
            else:
                li[k]=right[j]
                j=j+1 
                k=k+1 
        while i< len(left):
            li[k]=left[i]
            i=i+1 
            k=k+1 
            
        while j< len(right):
            li[k]=right[j]
            j=j+1 
            k=k+1 
            
li=[54,26,93,17,77,31,44,55,20]
mergesort(li)
print(li)
