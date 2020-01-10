#sort a list of tuples by second item
list=[(1,3),(2,3),(9,6),(0,1)]
print('list of tuples is'+' '+'=',list)
x=list.remove((1,3))
l=sorted(list)
l.append((1,3))
print('sorted list of tuples by second item'+' '+'=',l)



