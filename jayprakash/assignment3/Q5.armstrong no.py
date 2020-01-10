num=int(input('Enter any no.='))
n1=0
n2=1
count=0
if(num<=0):
    print('enter valid no,')

else:
    while(count<num):
        n3=n1+n2
        n1=n2
        print(n1)
        n2=n3
        count=count+1
