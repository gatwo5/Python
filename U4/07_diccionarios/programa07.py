cancion = {
    "nombre": 'blue',
    'artista': 'billie eilish',
    'album': 'hit me hard and soft',
    'produccion': 'Finneas'
}

cancion2 = {
    "nombre": 'wildflower',
    'fecha': 2025
}

fusion = cancion | cancion2

print(fusion)

cancion.update(cancion2)

print(cancion)

cancion_copia = cancion.copy()

print(id(cancion))
print(id(cancion_copia))