# armstronge number153

while True:
    n=int(input('enter the number'))
    sum=0
    data=n
    while (n>0):
        digit=n%10
        sum=sum+(digit*digit*digit)
        n=n//10
    if (data==sum):
        print('number is a armstronge')
    else:
        print('number is not a armstronge')
