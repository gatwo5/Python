cancion = {
    "nombre": 'blue',
    'artista': 'billie eilish',
    'album': 'hit me hard and soft',
    'produccion': 'Finneas'
}

for claves in cancion:
    print(claves)

for valores in cancion.values():
    print(valores)

for clave, valor in cancion.items():
    print(f'{clave} | {valor}')