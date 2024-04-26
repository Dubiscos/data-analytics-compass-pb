import random
import time
import os
import names
from animals import Animals

# Pergunta 1
random_int = [random.randint(1,1000) for _ in range(250)]
print("Lista:")
print(random_int)

random_int.reverse()
print("Lista reversa:")
print(random_int)

# Pergunta 2
animais = ["gato", "cachorro", "elefante", "tigre", "leao", "girafa", "panda", "macaco", "cavalo", "rato",
           "leopardo", "zebra", "passaro", "coelho", "canguru", "urso", "camelo", "tubarao", "lontra", "pinguim"]

animais.sort()
print("Lista animais:")
print(animais)

print("Animais:")
for animal in animais:
    print(animal)

with open("animais.csv", "w") as file:
    for animal in animais:
        file.write(animal + "\n")

# Pergunta 3
random.seed(40)

qtd_nomes_unicos = 3000
qtd_nomes_aleatorios = 10000000

aux = []
for i in range(0, qtd_nomes_unicos):
    aux.append(names.get_full_name())

print("Gerando {} nomes aleatórios".format(qtd_nomes_aleatorios))
dados = []

for i in range(0, qtd_nomes_aleatorios):
    dados.append(random.choice(aux))

with open("nomes_aleatorios.txt", "w") as file:
    for nome in dados:
        file.write(nome + "\n")

os.system("notepad nomes_aleatorios.txt")