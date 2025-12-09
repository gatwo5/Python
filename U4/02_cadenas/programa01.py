credenciales = "usuario:root|contraseña:123456"

usuario, contrasenia = credenciales.split('|')

usuario = usuario.split(':')[1]
contrasenia = contrasenia.split(":")[1]

print(usuario, contrasenia)
