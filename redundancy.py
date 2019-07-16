# Remove redundant elements from the sequence

def redundant(s):
    final='0'
    for char in s:
        if final[-1]!=char:
            final+=char
    return final[1:]
print(redundant('aaabbbdddccaaa'))
        
