def cifrado_cesar(frase, indice):
    alfabeto = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
    frase_cifrada = ''

    for caracter in frase:

        if(caracter == ' '):
            frase_cifrada += ' '
        else:
            caracter_cifrado = alfabeto.find(caracter.upper())

            if(indice + caracter_cifrado >= len(alfabeto)):
                caracter_cifrado = alfabeto[caracter_cifrado - len(alfabeto) + indice]
            else:
                caracter_cifrado = alfabeto[caracter_cifrado + indice]

            if (not caracter.isupper()):
                caracter_cifrado = caracter_cifrado.lower()

            frase_cifrada += caracter_cifrado

    return frase_cifrada

frase = input('Introduce una frase para cifrar: ')
indice = 0

while (indice < 1 or indice > 25):
    indice = int(input("Introduce el indice (1-25): "))

cifrado = cifrado_cesar(frase, indice)

print(f'La frase "{frase}" cifrada es "{cifrado}"')
