# 'Guess the number' game. Set an integer as the final answer and then ask the user to guess the number by taking the user's input.If the guess of the user is less than the final answer, print 'Your guess was less than the answer' and take input from the user again. Similarly, do the same if the guess is greater than the answer. If the guess is correct, print 'your guess is correct' and display the number of attempts. The program should keep on asking the user for his guess as long as he doesnt get the guess right.

v=50
c=0 
a=int(input('guess the no '))
while (a==v) or (a!=v):
    if (a==v):
        c=c+1
        print('correct!!! Total attempts:',c)
        break
    elif (a>v):
        c=c+1
        print('guess is greater')
        a=int(input('guess the no '))
    else:
        c=c+1
        print('guess is smaller')
        a=int(input('guess the no '))
        
