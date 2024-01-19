import json

with open('person.json', 'r') as arquivo_json:
    arquivo = json.load(arquivo_json)

print(arquivo)
