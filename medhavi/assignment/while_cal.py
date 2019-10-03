while True:
    a = int (input("enter first no "))
    b = int (input("enter second no"))
    #print("enter the choice")
    ch =int (input("enter the choice"))
    if(ch ==1):
        sum =a+b
        print(sum )
    if(ch ==2):
        sub = a-b
        print(sub)
    if(ch ==3):
        mult =a*b
        print(mult)
    if(ch ==4):
        div = a/b
        print(div)
    if(ch ==5):
        mod=a%b
        print(mod)
    if(ch==6):
        exp=a**b
        print(exp)
    if(ch==7):
        inte=a//b
        print(inte)
    if(ch==8):
        print('default')
        break
