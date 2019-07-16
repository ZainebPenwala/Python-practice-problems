# count the frequency of characters in the given string.

def freq(s):
    f={}
    for char in s:
        if char in f:
            f[char]+=1 
        else:
            f[char]=1 
    return f 
print(freq('hsdvjasjnjasbc'))
