# Write a Python program to combine two dictionary adding values for common keys

from collections import Counter
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}

d = Counter(d1) + Counter(d2)
print("first dictionary is>", d1 , end ="\n\n")
print("second dictionary is :>" ,d2 , end ="\n\n")
print("addition is :> ", d)