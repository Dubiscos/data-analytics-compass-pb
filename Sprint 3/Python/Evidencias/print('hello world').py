"""
from random import randint

def sortear_dado():
    return randint(1,6)

for i in range(1,7):
    if i % 2 == 1:
        continue

    if sortear_dado() == i:
        print('Acertou', i)
        break
else:
    print('Não acertou o número')
"""
"""def get_dia_semana(dia):
    dias ={
       1: 'Domingo',
       2: 'Segunda',
       3: 'Terça',
       4: 'Quinta',
       6: 'Sexta',
       7: 'Sábado',
    }
    return dias.get(dia, '** inválido **')

if __name__ =='__main__':
    for dia in range(0,9):
        print(f'{dia}: {get_dia_semana(dia)})')
  """
"""# Criando uma tupla
frutas = ("maçã", "banana", "laranja")

# Acessando elementos da tupla
print(frutas[0])  # Saída: maçã

# Iterando sobre a tupla
for fruta in frutas: 
        print(fruta)
# Saída:
# maçã
# banana
# laranja
 """
"""# Criando um dicionário
pessoa = {"nome": "Maria", "idade": 30, "cidade": "Exemplo"}

# Acessando valores por chave
print(pessoa["nome"])  # Saída: Maria
print(pessoa["idade"])  # Saída: 30

# Modificando valores
pessoa["idade"] = 31
pessoa["Sexo"] = "F"

# Adicionando um novo par chave-valor
pessoa["profissao"] = "engenheira"

for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")

del pessoa["idade"]

# Iterando sobre as chaves e valores do dicionário
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")
# Saída:
# nome: Maria
# idade: 31
# cidade: Exemplo
# profissao: engenheira
"""
nome = "Ana"
idade = 30

# Usando f-string para criar uma mensagem
mensagem = f"A pessoa se chama {nome} e tem {idade} anos."

# Exibindo a mensagem
print(mensagem)
# Saída: A pessoa se chama Ana e tem 30 anos.
