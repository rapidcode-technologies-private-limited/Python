#python program to count even and odd numbers in a list
while True:
    list= eval(input('enter element in [] :'))
    print(list)
    even_count=0
    odd_count=0
    #n=int(input('enter the range:'))
    for i in list:
        if i % 2==0:
            even_count=even_count+1
            #print('even'+' '+'number'+' '+'=',list[i])
        else:
            odd_count=odd_count+1
            #print('odd'+' '+'number'+' '+'=',list[i]) 
            
    print('count of even'+' '+'=',even_count)
    print('count of odd'+' '+'=',odd_count)
         
