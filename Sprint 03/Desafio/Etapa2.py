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

gross_sum = 0
movies_count = 0

for line in lines:
    data = analisar_linha_csv(line)
    data[0] = ajustar_nome_ator(data[0])
    gross_str = data[5].replace(',', '').replace('"', '').strip()
    try:
        gross = float(gross_str)
        gross_sum += gross
        movies_count += 1
    except ValueError:
        continue

average_gross = gross_sum / movies_count

with open('C:\\Users\\Dubiscos\\Documents\\Estagio\\Sprint 3\\Desafio\\etapa-2.txt', 'w') as file:
    file.write(f"Média de receita bruta dos principais filmes: ${average_gross:.2f}")
