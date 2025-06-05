# somar os quadrados dos pares que são multiplos de 6
from random import randint; from functools import reduce
num = [randint(1, 100) for _ in range(20)]
soma_num_pares_mul_6 = reduce(lambda x, y: x + y, list(map(lambda x: x ** 2, list(filter(lambda x: x % 2 == 0, list(filter(lambda x: x % 6 == 0, num)))))))
print(soma_num_pares_mul_6)