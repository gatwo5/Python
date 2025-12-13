def mysplit(cadena):
    lista_palabras = []
    palabra = ''

    for char in cadena:

        if (char == ' '):
            if (palabra != ''):
                lista_palabras.append(palabra)
                palabra = ''
        else:
            palabra += char

    if (palabra != ''):
        lista_palabras.append(palabra)

    return lista_palabras

cadena = 'When i come back around i dont know what to say'
lista_palabras = mysplit(cadena)

print(lista_palabras)