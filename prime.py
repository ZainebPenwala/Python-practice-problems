# print all the prime numbers in a given range.

for no in range (1,50):
    if no >1:
        for i in range(2,no):
            if(no%i)==0:
                break
        else:
          print(no)
