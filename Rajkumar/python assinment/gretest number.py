while True:
    num1=int(input('enter any 1st number'))
    num2=int(input('enter any second number'))
    num3=int(input('enter any third number'))
    if(num1>num2)&(num1>num3):
        print('number is greater',num1)
    elif(num2>num1)&(num2>num3):
        print('number is greater',num2)
    elif(num3>num1)&(num3>num2):
        print('number is greater',num3)
    else:
        print('number is equal')
