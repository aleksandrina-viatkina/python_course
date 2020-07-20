from itertools import count
from itertools import cycle
from itertools import islice

#задача а
for el in count(2):
    if el>20:
        break
    else:
        print(el)

#задача б
biography = ['Aleksandrina', 25, 13, 'август', 1994]
i=0
for el in cycle(biography):
    if i>4:
        break
    else:
        print(el)
        i+=1

'''Задача со * от преподавателя'''
new_list = [el for el in islice(count(1,2),5)]
iter = cycle(new_list)
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))


