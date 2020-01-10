#python program for sum of squares of first n natural numbers
while True:
    sum=0
    n=int(input('enter the number ='))
    for i in range(0,n):
        sq=i*i
        #print(sq)
        sum= sum+sq
    print('square' +' '+'sum'+' '+ 'of' +' '+' '+'number'+' ' '=',sum)
