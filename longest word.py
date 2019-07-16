# find_longest_word that takes a list of words and returns the length of the longest one.

li=['hi','hello','wonderful']
longest=li[0]
for elem in li[1:]:
    if len(elem)>len(longest):
        longest=elem
        
print(longest,len(longest))



# filter_long_words that takes a list of words and an integer n and returns the list of words that are longer than n

li=['hi','hello','wonderful']
n=3
f=[]
def filter_words (a,b):
    for elem in li:
        if len(elem)> n :
            f.append(elem)
    return f 
print(filter_words(li,n))
