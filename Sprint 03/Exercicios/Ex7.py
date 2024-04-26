a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

def numeros(list):
    impar = [numero for numero in list if numero % 2 != 0]
    return impar

lista_impar = numeros(a)

print(lista_impar)