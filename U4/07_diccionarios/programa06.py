cancion = {
    "nombre": 'blue',
    'artista': 'billie eilish',
    'album': 'hit me hard and soft',
    'produccion': 'Finneas'
}

del cancion['nombre']

print(cancion)
print(cancion.pop('artista'))
cancion.clear()
print(cancion)

cancion = {}
print(cancion)