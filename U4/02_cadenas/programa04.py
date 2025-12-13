def cifrar_cesar(frase):
    alfabeto = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
    frase_cifrada = ''

    for caracter in frase:
        
        if(caracter == ' '):
            frase_cifrada += ' '
        else:
            caracter_cifrado = alfabeto.find(caracter)

            if (alfabeto[caracter_cifrado] == 'Z'):
                caracter_cifrado = 'A'
            else:
                caracter_cifrado = alfabeto[caracter_cifrado + 1]

            frase_cifrada += caracter_cifrado
    
    return frase_cifrada

def descifrar_cesar(frase):
    alfabeto = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
    frase_descifrada = ''

    for caracter in frase:
        
        if(caracter == ' '):
            frase_descifrada += ' '
        else:
            caracter_descifrado = alfabeto.find(caracter)

            if (alfabeto[caracter_descifrado] == 'A'):
                caracter_descifrado = 'Z'
            else:
                caracter_descifrado = alfabeto[caracter_descifrado - 1]

            frase_descifrada += caracter_descifrado
    
    return frase_descifrada

# --- MAIN ---

cifrado = cifrar_cesar('AVE CAESAR')

print(cifrado)

descifrado = descifrar_cesar(cifrado)

print(descifrado)

