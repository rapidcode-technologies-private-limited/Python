num=int(input('enter a terms'))
num1=0
num2=1
count=0
if num<=0:
    print('enter a valid number')
else:
    while (count<num):
        nth=num1+num2
        num1=num2
        print(num1)
        num2=nth
        count=count+1
