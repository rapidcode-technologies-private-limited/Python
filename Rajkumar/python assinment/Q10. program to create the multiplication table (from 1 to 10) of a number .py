while True:
    num=int(input('enter a number'))
    if num>0:
        print('zero is not multipalication')
    for i in range(1,11):
        print(num,'*',i,'=',(num*i))
