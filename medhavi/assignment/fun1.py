#def fun(a, b = 100, c = 200):
 #   print('a is', a, 'b is', b, 'c is',c)
def fun(**phonenumbers):
    for name, phoneno in phonenumbers.items():
        print(name,phoneno)
