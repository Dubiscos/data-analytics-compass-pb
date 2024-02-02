# PROGRAMAÇÃO FUNCIONAL  
É um paradigma de programação que trata a computação como uma avaliação de funções matemáticas e evita a mudança de estado e a mutabilidade de dados.  
Funções Puras: Uma função pura retorna o mesmo resultado para as mesmas entradas e não tem efeitos colaterais.  
Exemplo:  
def soma(a, b):  
    return a + b  

Imutabilidade: Dados não podem ser alterados após serem criados. Em vez de modificar dados, você cria novos dados com base nos existentes.  
Exemplo:  
lista_original = [1, 2, 3]  
nova_lista = lista_original + [4, 5]  

Funções de Ordem Superior: Funções que aceitam outras funções como argumentos ou retornam funções.  
Exemplo:  
def aplicar_funcao(funcao, lista):  
    return [funcao(x) for x in lista]  
quadrados = aplicar_funcao(lambda x: x**2, [1, 2, 3, 4])  

Recursão: O uso de funções que chamam a si mesmas para resolver um problema.  
Exemplo:  
def fatorial(n):  
    if n == 0 or n == 1:  
        return 1  
    else:  
        return n * fatorial(n - 1)  

Mapeamento, Redução e Filtragem: Operações comuns em listas que são usadas para transformar, combinar e filtrar dados.  
Exemplo:  
numeros = [1, 2, 3, 4, 5]  
quadrados = list(map(lambda x: x**2, numeros))  
soma = reduce(lambda x, y: x + y, numeros)  
pares = list(filter(lambda x: x % 2 == 0, numeros))  

função de alta ordem em programação funcional é uma função que aceita outras funções como argumentos ou retorna funções como resultados. Isso permite uma maior abstração e flexibilidade no código. Vamos explorar alguns exemplos simples em Python:  

Função como Argumento:  
def aplicar_funcao(funcao, valor):    
    return funcao(valor)    

def dobro(x):    
    return 2 * x    

resultado = aplicar_funcao(dobro, 5)  
print(resultado)   

Neste exemplo, aplicar_funcao é uma função de alta ordem que aceita outra função (dobro) como argumento e a aplica a um valor específico.  

Função como Resultado:  
def criar_multiplicador(fator):  
    def multiplicar(x):  
        return fator * x  
    return multiplicar  

dobrar = criar_multiplicador(2)  
triplicar = criar_multiplicador(3)  

print(dobrar(5))   
print(triplicar(5))   
Neste exemplo, criar_multiplicador é uma função de alta ordem que retorna outra função (multiplicar). Isso permite criar funções especializadas com base em diferentes fatores.  

Funções Integradas de Alta Ordem: Python possui funções integradas de alta ordem, como map, filter e reduce:  
Exemplo com map:  
numeros = [1, 2, 3, 4]  
quadrados = list(map(lambda x: x**2, numeros))  
print(quadrados)  # Saída: [1, 4, 9, 16]  

Exemplo com filter:  
pares = list(filter(lambda x: x % 2 == 0, numeros))  
print(pares)  # Saída: [2, 4]  

Exemplo com reduce (precisa ser importado do módulo functools):  
from functools import reduce  
soma = reduce(lambda x, y: x + y, numeros)  
print(soma)  
Closure: é uma função que "encapsula" variáveis do escopo circundante no qual foi definida. Em outras palavras, a closure tem acesso a variáveis que não estão diretamente em seu escopo, mas que estão presentes no escopo onde a closure foi criada.  
Exemplo:   
def multiplicador(x):  
    def interna(y):  
        return x * y  
    return interna  

# Criando closures  
dobrar = multiplicador(2)  
triplicar = multiplicador(3)  

# Usando closures  
print(dobrar(5))   # Saída: 10  
print(triplicar(5)) # Saída: 15  
Lambda: A função lambda é uma maneira de criar funções anônimas que não precisam ser definidas usando a palavra-chave def. As funções lambda são úteis quando você precisa de uma função simples por um curto período e não quer criar uma função completa usando def.  
Sintaxe básica: lambda arg: expressão  
