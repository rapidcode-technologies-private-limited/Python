    # armstorong number 153 (1+5+3)
while True:
    n=int(input('enter a number'))
    data=n
    rev=0
    while (n>0):
        rem=n%10
        rev=rev*10+rem
        n=n//10
    if(data==rev):
        print('number is  palindrom')
    else:
        print('number is not palindrom')
            
            
                  
        
