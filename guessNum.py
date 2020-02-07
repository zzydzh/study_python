from random import randint
x = randint(0,300)
for count in range(0,10):
    print('please input a number between 0~300:')
    digit = int(input())
    if digit > x:
        print('too large,try again:')
    elif digit==x:
        print('Bingo')
        break
    else:
        print('too small,try again:')
        
        
