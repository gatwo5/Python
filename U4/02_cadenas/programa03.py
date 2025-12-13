cadena = "Organización de las Naciones Unidas"
cadena = cadena.split(' ')

mayusuculas = ''
minusculas = ''

for palabras in cadena:

    if (palabras[0].isupper()):
        mayusuculas += palabras[0]
    else:
        minusculas += palabras + ' '

print(mayusuculas)
print(minusculas)
