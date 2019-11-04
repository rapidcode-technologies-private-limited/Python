while True:
    m=int(input('Enter a month='))
    if(m==1):
        print('January')
        
    elif(m==2):
        print('February')
        
    elif(m==3):
        print('March')
        
    elif(m==4):
        print('Aprial')
        
    elif(m==5):
        print('May')
        
    elif(m==6):
        print('June')
        d=int(input('Enter a day='))
        if(d<=30):
            print('spring')
        else:
            print('not a spring')
    elif(m==7):
        print('July')
        d=int(input('Enter a day='))
        if(d<=31):
            print('spring')
        else:
            print('not a spring')
    elif(m==8):
        print('August')
        d=int(input('Enter a day='))
        if(d<=31):
            print('spring')
        else:
            print('not a spring')
    elif(m==9):
        print('September')
    elif(m==10):
        print('October')
    elif(m==11):
        print('November')
    elif(m==12):
        print('December')
