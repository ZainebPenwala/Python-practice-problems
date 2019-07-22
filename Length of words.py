# A program that maps a list of words into a list of integers representing the lengths of the correponding words.

li=['hello','wonderful','beauty','watermeleon']
length=[]
for elem in li:
    length.append(len(elem))
print(length)
