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

actors_data = []

for line in lines:
    data = analisar_linha_csv(line)
    data[0] = ajustar_nome_ator(data[0])
    actor = data[0]

    total_gross_str = data[1].replace(',', '').replace('"', '').strip()

    try:
        total_gross = float(total_gross_str)
        actors_data.append((actor, total_gross))
    except ValueError:
        continue

sorted_actors_data = sorted(actors_data, key=lambda x: (-x[1], x[0]))

with open('C:\\Users\\Dubiscos\\Documents\\Estagio\\Sprint 3\\Desafio\\etapa-5.txt', 'w') as file:
    for actor, total_gross in sorted_actors_data:
        file.write(f"{actor} - ${total_gross:.2f}\n")
