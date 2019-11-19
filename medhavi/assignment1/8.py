#python program to print all odd numbers in range 
while True:
    r=int(input('enter the range'))
    for i in range(0,r):
        if i%2!=0:
            print('odd'+' '+'number'+' '+'=',i)
