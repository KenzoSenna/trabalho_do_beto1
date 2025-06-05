from random import randint
from functools import reduce
numeros = [randint(1, 100) for _ in range(15)]
quadrados_dos_pares = reduce(lambda x, y: x + y, map(lambda x: x ** 2, list(filter(lambda x: x % 2 == 0, numeros)))) / len(map(lambda x: x ** 2, list(filter(lambda x: x % 2 == 0, numeros))))
print(quadrados_dos_pares)