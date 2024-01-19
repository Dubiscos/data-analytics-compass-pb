class Ordenadora:
    def __init__(self, lista_baguncada):
        self.listaBaguncada = lista_baguncada

    def ordenacaoCrescente(self):
        self.listaBaguncada = sorted(self.listaBaguncada)
        pass

    def ordenacaoDecrescente(self):
        self.listaBaguncada = sorted(self.listaBaguncada, reverse=True)
        pass

lista_crescente = [3, 4, 2, 1, 5]
lista_decrescente = [9, 7, 6, 8]

crescente = Ordenadora(lista_crescente)
decrescente = Ordenadora(lista_decrescente)

crescente.ordenacaoCrescente()
decrescente.ordenacaoDecrescente()

print(crescente.listaBaguncada)
print(decrescente.listaBaguncada)
