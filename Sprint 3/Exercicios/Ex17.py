def divisao(lista):
    tamanho = len(lista)
    partes = tamanho // 3

    parte1 = lista[:partes]
    parte2 = lista[partes:2*partes]
    parte3 = lista[2*partes:]

    return parte1, parte2, parte3

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
resultado = divisao(lista)
print(resultado[0], resultado[1], resultado[2])
