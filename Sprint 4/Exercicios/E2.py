def conta_vogais(texto: str) -> int:
    vogal = lambda x: x.lower() in 'aeiou'
    numero_vogais = len(list(filter(vogal, texto)))
    return numero_vogais
   