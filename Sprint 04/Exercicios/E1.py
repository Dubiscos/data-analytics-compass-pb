caminho_arquivo = 'C:\\Users\\Dubiscos\\Documents\\Estagio\\Sprint 4\\Exercicios\\number.txt'

def ler_numeros(arquivo):
    with open(arquivo, 'r') as arquivo:
        return list(map(int, arquivo.readlines()))

def maiores_pares_e_soma(numeros):
    numeros_pares = filter(lambda x: x % 2 == 0, numeros)
    maiores_pares = sorted(numeros_pares, reverse=True)[:5]
    soma_maiores_pares = sum(maiores_pares)
    return maiores_pares, soma_maiores_pares

numeros = ler_numeros(caminho_arquivo)

maiores_pares, soma_maiores_pares = maiores_pares_e_soma(numeros)

print('Os 5 maiores números pares em ordem decrescente:', maiores_pares)
print('A soma destes valores:', soma_maiores_pares)
