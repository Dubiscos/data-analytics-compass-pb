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

arquivo_csv = 'C:\\Users\\Dubiscos\\Documents\\Estagio\\Sprint 3\\Desafio\\actors.csv'

with open(arquivo_csv, 'r', encoding='utf-8') as file:
    lines = file.readlines()

    header = lines[0]
    lines = lines[1:]

max_movies_actor = ""
max_movies_count = 0

for line in lines:
    data = analisar_linha_csv(line.strip())
    
    if len(data) >= 3:

        actor = data[0].replace('"', '')
        actor = ajustar_nome_ator(actor)

        movies_count = int(data[2].replace(',', '').strip())

        if movies_count > max_movies_count:
            max_movies_count = movies_count
            max_movies_actor = actor

with open('C:\\Users\\Dubiscos\\Documents\\Estagio\\Sprint 3\\Desafio\\etapa-1.txt', 'w') as file:
    file.write(f"{max_movies_actor} - {max_movies_count} filmes")
