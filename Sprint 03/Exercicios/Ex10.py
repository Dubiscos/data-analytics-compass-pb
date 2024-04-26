def duplicado(lista):
    return list(set(lista))

lista_a = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']
lista_b = duplicado(lista_a)

print(lista_b)