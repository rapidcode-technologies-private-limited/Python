num=int(input("enter the terms"))
n1=0
n2=1
count=0
if num<=0:
    print("enter a valid number ")
else:
    while (count<num):
        nth=n1+n2
        n1=n2
        print(n1)
        n2=nth
        count=count+1 
