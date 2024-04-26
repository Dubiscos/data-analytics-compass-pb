from functools import reduce

def calcula_saldo(lancamentos) -> float:
    mapear_valor = lambda lancamento: lancamento[0] if lancamento[1] == 'C' else -lancamento[0]
    valores_mapeados = map(mapear_valor, lancamentos)
    saldo_final = reduce(lambda x, y: x + y, valores_mapeados, 0)
    return saldo_final

lancamentos = [
    (200, 'D'),
    (300, 'C'),
    (100, 'C')
]
print(calcula_saldo(lancamentos))
