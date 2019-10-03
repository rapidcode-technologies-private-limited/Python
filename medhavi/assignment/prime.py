count=0
i=2

while True:
    n=int(input("Enter number: "))    
    
    while i <= n/2:
        if n%i==0:
            count +=1
            break
        i +=1

    if n==1:
        print("number is niether prime nor composite")
    elif count==0:
        print("number is prime")
    else:
        print("number is not prime")
    
    count=0
    i=2
