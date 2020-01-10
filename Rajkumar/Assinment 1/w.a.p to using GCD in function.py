    #w.a.p to using GCD in function:

while True:
    def GCD(a,b):
        if b==0:
            return a
        else:
            return GCD (b,a%b)
    n1=int(input('enter a frist number'))
    n2=int(input('enter a second number'))
    print(GCD(n1,n2))
