class Calculo:
    def somar(self, x, y):
        resultado = x + y
        return resultado

    def subtrair(self, x, y):
        resultado = x - y
        return resultado

x = 4
y = 5

calculo = Calculo()

soma = calculo.somar(x, y)
print(f"Somando: {x} + {y} = {soma}")

subtracao = calculo.subtrair(x, y)
print(f"Subtraindo: {x} - {y} = {subtracao}")
