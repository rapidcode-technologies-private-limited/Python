
n = int (input("enter the number"))
print('Entered Number is ' + str(n))

rev=0
m=n

while n>0:
    d=n%10
    rev=rev*10+d
    n=n//10
    print(rev)

print('m= '+str(m))
print('rev= '+str(rev))

if rev==m:
    print("number is palendrome")
else:
    print("number is not palendrome")
