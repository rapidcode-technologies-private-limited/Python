#python program for cube sum of first n natural numbers
while True:
    sum=0
    n=int(input('enter the number'))
    for i in range(0,n):
        cube=i*i*i
        #print(sq)
        sum= sum+cube
    print('cube' +' '+'sum'+' '+ 'of' +' '+' '+'number'+' ' '=',sum)
