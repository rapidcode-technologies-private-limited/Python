while True:
    n=int(input("enter the number"))
    count=0
    i=1

    while i<=n:
        if n%i==0:
            count +=1
        #print('count= ' +str(count))
        i +=1

    if count==2:
        print("number is prime")
    else:
        print("number is not prime")
    count=0
