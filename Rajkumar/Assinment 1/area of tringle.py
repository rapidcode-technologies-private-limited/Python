while True:
    import math
    a=int(input('enter any frist side of the traigle'))
    b=int(input('enter any second side of the traigle'))
    c=int(input('enter any third side of the traigle'))
    s=(a+b+c)/2
    area=math.sqrt(s*(s-a)*(s-b)*(s-c))
    print('area is traingle is',area)
