# calcular o poduto dos numeros pares apos multiplicar por 2
from functools import reduce
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
produto = reduce(lambda x, y: x / y, list(filter(lambda x: x % 2 == 0, list(map(lambda x: x * 2, num)))))
print(produto)