diccionario = {}

print(type(diccionario))

persona = {
    "nombre": "daniel",
    "edad": 20,
    "pais": "España"
}

for clave, valor in persona.items():
    print(f'{clave} : {valor}')
    print(type(valor))
    print()