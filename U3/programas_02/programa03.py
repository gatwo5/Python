import platform, os

print('Procesador:', platform.processor())
print('SO y Version:', platform.system(), platform.version())
print('Nombre host:', platform.node())
print('Directorio actual:',os.getcwd())