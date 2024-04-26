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

max_average_actor = ""
max_average_gross = 0

for line in lines:
    data = analisar_linha_csv(line)
    data[0] = ajustar_nome_ator(data[0])
    average_gross_per_movie = float(data[3].replace(',', ''))

    if average_gross_per_movie > max_average_gross:
        max_average_gross = average_gross_per_movie
        max_average_actor = data[0]

with open('C:\\Users\\Dubiscos\\Documents\\Estagio\\Sprint 3\\Desafio\\etapa-3.txt', 'w') as file:
    file.write(f"{max_average_actor} - Maior média de receita por filme: ${max_average_gross:.2f}")
