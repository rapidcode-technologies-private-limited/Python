#w.a.p swapping two number in function using

def swappingnumber(n1,n2):
    temp=n1
    n1=n2
    n2=temp
    print('before swapping')
    print('N1:'+str(n1))
    print('N2:'+str(n2))
n1=int(input('enter frist variable'))
n2=int(input('enter second variable'))
print('after swapping')
print('N1:'+str(n1))
print('N2:'+str(n2))
swappingnumber(n1,n2)
    
