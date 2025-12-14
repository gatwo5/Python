cancion = {
    "nombre": 'blue',
    'artista': 'billie eilish',
    'album': 'hit me hard and soft',
    'produccion': 'Finneas'
}

print(cancion['nombre'])
print(cancion['album'])

print(cancion.get('produccion'))
print(cancion.get('fecha'))
print(cancion.get('fecha','No disponible'))