from functools import reduce
from random import randint
num = [randint(1, 500) for _ in range(10)]
maiornum_impar = reduce(lambda y, x: x if x > y else y, list(filter(lambda x: x % 2 != 0, num)))
print(maiornum_impar)