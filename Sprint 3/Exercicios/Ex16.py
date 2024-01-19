def soma(string_numeros):
    numeros = [int(numero) for numero in string_numeros.split(',')]
    soma = sum(numeros)
    return soma

string_numeros = "1,3,4,6,10,76"

resultado = soma(string_numeros)
print(f"{resultado}")
