abc =100
def fun():
    global abc
    abc =5
    print("abc in the fun",abc)

fun()
print("abc outside of the fun",abc)
