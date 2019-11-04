while True:
    num=int(input('enter any number'))
    if num>0:
        print('number is not valide')
        for i in range(1,11):
            print(num,"*",i,"=",(num*i))
