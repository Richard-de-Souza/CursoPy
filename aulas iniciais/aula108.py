from itertools import count

c1= count(start= 3, step=5)
#count é um iterator e conta eternamente
#diferente do range

for i in c1:
    if i>100:
        break
    print(i)
print('c1', hasattr(c1, '__iter__'))
print('c1', hasattr(c1, '__next__'))