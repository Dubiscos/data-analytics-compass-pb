import pandas as pd
import numpy as np

def analisar_linha_csv(line):
    valores = []
    aspas = False
    valor_atual = ''

    for caractere in line:
        if caractere == ',' and not aspas:
            valores.append(valor_atual)
            valor_atual = ''
        elif caractere == '"':
            aspas = not aspas
        else:
            valor_atual += caractere
    
    valores.append(valor_atual)
    return valores

arquivo_csv = '/home/ubuntu/Downloads/actors.csv'

with open(arquivo_csv, 'r', encoding='utf-8') as file:

    df = pd.read_csv(arquivo_csv)

    # Pergunta 1
    filmes_ator_num = df.loc[df['Number of Movies'].idxmax()]
    filmes_ator_nome = filmes_ator_num['Actor']
    num_filmes = filmes_ator_num['Number of Movies']

    print("Ator/Atriz com mais filmes:", filmes_ator_nome)
    print("Numero de filmes:", num_filmes)

    # Pergunta 2
    media_filmes = np.mean(df['Number of Movies'])

    print("Média de filmes:", round(media_filmes))

    # Pergunta 3
    media_ator = df.loc[df['Average per Movie'].idxmax()]
    media_por_nome = media_ator['Actor']

    print("Ator/Atriz com maior média por filme:", media_por_nome)

    # Pergunta 4
    filmes = df['#1 Movie'].mode() # metodo mode retorna o valor mais frequente da coluna
    filmes_frequencia = df['#1 Movie'].value_counts().max() # contagem de valore unicos e frequencia max

    print("Filme(s) mais frequente(s) é", filmes.to_list(), "com frequência de:", filmes_frequencia)
