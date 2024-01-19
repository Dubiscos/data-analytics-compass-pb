def my_map(list, f):
    return [f(elemento) for elemento in list]

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
potencia = lambda x: x ** 2

resultado = my_map(a, potencia)
print(resultado)
