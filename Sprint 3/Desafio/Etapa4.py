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

def ajustar_nome_ator(nome):
    return nome.replace("Robert Downey, Jr.", "Robert Downey Jr")

with open('C:\\Users\\Dubiscos\\Documents\\Estagio\\Sprint 3\\Desafio\\actors.csv', 'r', encoding='utf-8') as file:
    lines = file.readlines()

header = lines[0]
lines = lines[1:]
movie_count_dict = {}

for line in lines:
    data = analisar_linha_csv(line)
    movie = data[4]
    movie_count_dict[movie] = movie_count_dict.get(movie, 0) + 1

sorted_movie_count = sorted(movie_count_dict.items(), key=lambda x: (-x[1], x[0]))

with open('C:\\Users\\Dubiscos\\Documents\\Estagio\\Sprint 3\\Desafio\\etapa-4.txt', 'w') as file:
    for rank, (movie, count) in enumerate(sorted_movie_count, start=1):
        file.write(f"{rank} - O filme \"{ajustar_nome_ator(movie)}\" aparece {count} vezes no dataset\n")
