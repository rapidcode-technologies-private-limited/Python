while True:
    n=int(input('Enter any no.='))
    fact=1
    if n<0:
        print('Valid no.')

    elif n==1:
        print('factorial no.is 1')

    else:
        for i in range(1,n+1):
            fact=fact*i
    print('factorial no.is',fact)
