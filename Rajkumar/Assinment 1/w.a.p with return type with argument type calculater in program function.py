    #w.a.p with return type with argument type calculater in program function:

while True:
    def add(n1,n2):
        return(n1+n2)
    def sub(n1,n2):
        return(n1-n2)
    def multi(n1,n2):
        return(n1*n2)
    def div(n1,n2):
        return(n1/n2)
    def rem(n1,n2):
        return(n1%n2)
    print('1:addition')
    print('2:subtraction')
    print('3:multipalication')
    print('4:division')
    print('5:remnder')
    n1=int(input('enter a number'))
    n2=int(input('enter b number'))
    choise=int(input('enter any choise.1/2/3/4/5'))
    if choise==1:
        sum=add(n1,n2)
        print(sum)
    elif choise==2:
        sub=sub(n1,n2)
        print(sub)
    elif choise==3:
        multi=multi(n1,n2)
        print(multi)
    elif choise==4:
        div=div(n1,n2)
        print(div)
    elif choise==5:
        rem=rem(n1,n2)
        print(rem)
    else:
        print('wrong choise')







        
