#Generating random strings untill a given string is generated
import random
def statement(n):
    print('Rec: ' + str(n))
    if n==1:
        return ('xyz')
    if(n==2):
        return ('how')
    if(n==3):
        return ('hi, how are you')
while True:
    data=statement(random.randint(1,3))
    print(data)
    if(data=='hi, how are you'):
        break
    print(data)
