import csv

arquivo_csv = 'C:\\Users\\Dubiscos\\Documents\\Estagio\\Sprint 4\\Exercicios\\estudantes.csv'

def dado_estudante(estudante):
    nome = estudante[0]
    notas = list(map(int, estudante[1:]))
    tres_maiores_notas = sorted(notas, reverse=True)[:3]
    media = round(sum(tres_maiores_notas) / 3, 2)
    return f"Nome: {nome} Notas: {tres_maiores_notas} Média: {media}"

def relatorio(arquivo):
    with open(arquivo, 'r', encoding='utf-8-sig') as arquivo:
        leitor = csv.reader(arquivo)
        linhas = list(leitor)
        linhas_ordenadas = sorted(linhas, key=lambda x: x[0])
        for linha in linhas_ordenadas:
            print(dado_estudante(linha))

relatorio(arquivo_csv)