i = int(input('enter row'))
j = int(input('enter column'))
'''for i in range(len(row)):
  for j in range(len(row[i])):
        print(row[i][j], end= ' ')'''
row,col=(i,j)
arr=[[i,j]*col*row]
print(arr[i][j],end=' ')
