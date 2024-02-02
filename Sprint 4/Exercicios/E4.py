def calcular_valor_maximo(operadores, operandos) -> float:
    mapeamento_operacoes = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
        '%': lambda x, y: x % y
    }
    resultados = [mapeamento_operacoes[operadores](*operandos) for operadores, operandos in zip(operadores, operandos)]
    maior_valor = max(resultados)
    return maior_valor

operadores = ['+','-','*','/','+']
operandos = [(3,6), (-7,4.9), (8,-8), (10,2), (8,4)]

print(calcular_valor_maximo(operadores, operandos))
