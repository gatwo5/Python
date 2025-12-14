diccionario = {
    'persona' : {'direccion': 'calle preciados',
                 'numero': 20}
}
print(diccionario['persona']['numero'])

familia = {
    'padre' : {
        'edad': 50,
        'nombre': 'Juan'
    },

    'madre' : {
        'edad': 50,
        'nombre': 'Juanita'
    },

    'hijo' : {
        'edad': 20,
        'nombre': 'Pepito'
    }
}

for clave, valor in familia.items():
    print(f'{clave} | {valor}')