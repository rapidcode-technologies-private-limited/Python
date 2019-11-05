a=int(input('enter integer'))
b=bool(int(input('enter Boolean add 0 for false')))
def star(a,b):
    if b==True:
        c=1
        while 0<=a:
            print(c *'*')
            c=c+1
    else:
        while a>0:
            print(a *'*')
            a=a-1
star(a,b)            
