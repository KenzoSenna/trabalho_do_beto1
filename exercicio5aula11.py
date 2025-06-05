from functools import reduce
from random import randint
num = [randint(1, 10) for _ in range(10)]
lista_maioresque_5_quadrado = list(filter(lambda x: x > 5, list(map(lambda x: x ** 2, num))))
media = reduce(lambda x, y: x + y, lista_maioresque_5_quadrado) / len(lista_maioresque_5_quadrado)