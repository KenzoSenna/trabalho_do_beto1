### aprendendo sobre filter e map
import random
numeros = [1, 2, 3, 4, 5, 6, 7]
pares = tuple(filter(lambda x: x % 2 == 0, numeros))
print(pares)

lista_randomica = [random.randint(20, 100) for _ in range(100)]
media = sum(lista_randomica) / len(lista_randomica)
numeros_randomicos = list(filter(lambda x: x > 60, lista_randomica)) 
print(numeros_randomicos)
filtrada_media = list(filter(lambda x: x > media, lista_randomica))
 
#sorted(pessoas, key = lambdaFunction lambda x: x[1])
pessoas = [("Ana", 19), ("João", 30), ("Maria"), 20]