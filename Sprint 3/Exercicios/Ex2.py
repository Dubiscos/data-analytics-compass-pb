lista_numero = [int(input(f"Digite o {i + 1}º número: ")) for i in range(3)]

for numero in lista_numero:
    if numero % 2 == 0:
        print(f"Par: {numero}")
    else:
        print(f"Ímpar: {numero}")
        