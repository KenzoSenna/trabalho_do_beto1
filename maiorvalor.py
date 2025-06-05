from functools import reduce
from random import randint

num = [randint(1, 500) for _ in range(10)]
maiornum = reduce(lambda y, x: x if x > y else y, num)
print(maiornum)
soma_total = reduce(lambda x, y: x + y, num)
#print(soma_total)