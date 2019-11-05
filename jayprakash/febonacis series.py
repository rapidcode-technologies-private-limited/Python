while True:
    def feb(n):
        a=0
        b=1
        if n==0:
            print(n)
        elif n==1:
            print(a)
        else:
            print(a)
            for i in range(2,n+1):
                c=a+b
                a=b
                b=c
                print(c)
    n=int(input('enter any number'))
    feb(n)
