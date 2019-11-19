#python dictionary with keys having multiple inputs
d1={'a':'1,5','b':12,'c':11}
for data1,data2 in d1.items():
    print(str(data1)+':'+str(data2))
d=d1.clear()
print(d1)
