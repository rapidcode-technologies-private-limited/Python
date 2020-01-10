while True:
    n1=int(input('Enter any no.of n1='))
    n2=int(input('Enter any no.of n2='))
    n3=int(input('Enter any no.of n3='))
    if (n1>n2 and n1>n3) :
        print('n1 is gratest no.',n1)

    elif (n2>n1 and n2>n3) :
        print('n2 is gratest no.',n2)

    elif (n3>n1 and n3>n3):
        print('n3 is gratest no.',n3)

    else:
        print('All no. is equal')
        
