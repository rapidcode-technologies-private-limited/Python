count=0
i=2
while True:
    n=int(input('enter a number'))
    while i<=n/2:
        if n%2==0:
            count=count+1
            break
        i=i+1
    if(n==1):
        print('number is nither prime nor compositive')
    elif(count==0):
        print('number is a prime')

    else:
        print('number is not prime')
    count=0
    i=2
    
