import random

random_list = random.sample(range(500), 50)

ordernar = sorted(random_list)
tamanho = len(random_list)
meio = tamanho // 2
if tamanho % 2 == 0:
    mediana = (ordernar[meio - 1] + ordernar[meio]) / 2
else:
    mediana = ordernar[meio]

media = sum(random_list) / tamanho
valor_minimo = min(random_list)
valor_maximo = max(random_list)

print(f"Media: {media}, Mediana: {mediana}, Mínimo: {valor_minimo}, Máximo: {valor_maximo}")
