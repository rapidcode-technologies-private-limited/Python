while True:
    fact=1
    print('enter a number')
    num=int(input())
    
    if num<0:
        print('enter a valid number')
    elif num==1:
        print('factorial is 1')
    else:
        for i in range(1,num+1):
            fact=fact*i
            print('factorial is',fact)
