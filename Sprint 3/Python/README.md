## Matéria
Python

## Relatório diários

#### relatorio dia 1

Peguei o dia para dar continuidade no curso de Cyberseguranã terminando todas as configurações básicas para utilizar e li um pouco da apostila de Python.

#### relatorio dia 2

Foi feito a instalação do python, Anacadonda em Windows e Linux, tive mais problemas na instalação no linux por questão da memoria interna da VM, o anaconda ficou pesado para a capacidade disponivel, só que foi resolvido.

#### relatorio dia 3

comecei os fundamentos e a forma de logica do python, seguindo com alguns comandos basicos e suas formulas numericas, fiquei com duvida sobre o funcionamento do BuiltIn do python. resolvi alguns exercicios propostos no modulo de python da seção 5

#### relatorio dia 4

Teve a explicação do funcionamento de estruturas de controle como if, else, while e for., eu tinha um conhecimento previo no C# então tive mais facil para entender o funcionamento e quando utilizar e depois  como fazer leitura de arquivos CSV e rodar os arquivos pelo python

#### relatorioa dia 5

Comecei a seção de comprehension, tive um pouco de dificuldade no inicio porem dps que consegui entender melhor a base de dicionario, lista e gerador ficou mais facil essa seção e terminei a sdeção de funções.

#### relatorioa dia 8

Finalizei o curso de python no qual faltava seção de Programção orientada a objetos(POO),gerenciamento de pacotes e isolamente de ambiente. Essa seção deu para compreender o básico de POO e como utilizar em alguns casos, porêm ainda sinto que tenho q revisar para enteder melhor.

#### relatorioa dia 9

Comecei os exercicios da AWS 3/10. A primeira parte dos exercicios e senti que foi bem tranquilo, pois não exigia uma resposta elabora e alguns codigos de poucas linhas já conseguia resolver os problemas e foi bom que consegui ver que consigo escrever códigos simples em python e parei no inicio da parte 2.

#### relatorioa dia 10

Segui resolvendo ox exercicos da parte 2 e alguns já comecei a ter mais dificuldade para entender o que o exercicio queria e como resolver, porem consegui terminar os exercicos da parte 2 e começar o desafio de ETL, só que nesse desafio já senti muito mais dificuldade sem a utilização de bibliotecas e acabei travando na etapa 1 pela questão no nome do Robert Downey Jr que possuia virgula e ponto.

#### relatorioa dia 11

Passei o dia resolvendo os exercicios do ETL e consegui depois de algumas horas achar a solução para a leitura da base sem importar biblioteca e consegui resolver os exercicios.

#### relatorioa dia 12

Revisei meus códigos para o envio e ajustei as pastas para subir no Git os arquivos para o repositório.

# Anotações

__builtins__ = é um módulo especial que contém funções e tipos incorporados que estão sempre disponíveis globalmente. Não precisa se preocupar em acessar __builtins__ diretamente, pois as funções e tipos incorporados são automaticamente disponíveis no escopo global. 

Tuplas = As tuplas são similares a lista porém elas são imutáveis, e portanto não podem receber alterações

*args (Argumentos posicionais): Permite que uma função aceite um número variável de argumentos posicionais. O asterisco * antes de "args" indica que a função pode receber vários argumentos, que serão tratados como uma tupla.
Ex: def exemplo_args(*args):
    for arg in args:
        print(arg)
exemplo_args(1, 2, "Python")

**kwargs (Argumentos de palavra-chave): Permite que uma função aceite um número variável de argumentos de palavra-chave (ou seja, argumentos nomeados). O duplo asterisco ** antes de "kwargs" indica que a função pode receber vários argumentos de palavra-chave, que serão tratados como um dicionário.

Ex: def exemplo_kwargs(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

exemplo_kwargs(nome="Alice", idade=25, cidade="Exemplo")

Combinação de ambos: Você pode usar *args e **kwargs na mesma função para aceitar uma combinação de argumentos posicionais e de palavra-chave.

Ex: ef exemplo_combinado(arg1, *args, **kwargs):
    print(f"Argumento 1: {arg1}")
    print(f"Outros argumentos posicionais: {args}")
    print(f"Argumentos de palavra-chave: {kwargs}")

exemplo_combinado("Python", 2, 3, nome="Alice", idade=25)

Operadores binários

| = union 
& = intersection 
- = difference
^ = symmetric_difference

Operadores relacionais

<= issubset
>= issuperset 

Operadores de atribuição

|= = update
&= = intersection_update
-= = difference_update
^= = symmetric_difference_update

