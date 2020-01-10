'''n=int(input('enter the rows'))
for i in range(n):
    for j in range(i+1):
        print('*',end=' ')
    print()
for i in range(n-1):
    for j in range(n-i-1):
        print('*',end=' ')
    print()'''




for i in range(5):
    for j in range(i+1):
        print('*',end=' ')
    print()
for i in range(5):
    for j in range(5-i-1):
        print('*',end=' ')
    print()
