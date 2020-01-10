def add(x,y):
    sum = x+y
    if sum in range(15,20):
        return 20
    else:
        return sum
while True:    
    a=int(input('enter the first number'))
    b=int(input('enter the second number'))
    sum=add(a,b)
    print('sum'+'=',sum)



        

    
