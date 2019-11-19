#python program to print even length words in a string
while True:
    string =input('enter string : ')
    l=len(string)
    print(l)
    if l%2==0:
        print('string is even length')
        print('even'+' '+'length'+' '+'word'+' '+'=',string)
    else:
        print('string is odd length')
