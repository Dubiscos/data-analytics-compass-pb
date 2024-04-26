import hashlib

while True:
    entrada = input("Digite uma palavra para gerar o hash ou digite 'sair' para encerrar: ")
    if entrada.lower() == 'sair':
        break

    hash = hashlib.sha1()
    hash.update(entrada.encode())
    resultado = hash.hexdigest()

    print("Hash SHA-1 da entrada:", resultado)
