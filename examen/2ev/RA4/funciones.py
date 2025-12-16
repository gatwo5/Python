# == crear_inventario==

# No recibe nada para crear un inventario vacío
# Devuelve un diccionario vacío

def crear_inventario():

    # Crea un inventario vacio

    return {}

# == agregar_producto() ==

# Recibe el inventario, el código del producto, su nombre y su precio inicial para crear un nuevo producto
# Devuelve False si el código existe y True si no existe

def agregar_producto(inventario, codigo, nombre, precio_inicial):

    codigo_no_existente = False

    # Si el código no existe en el inventario lo crea

    if codigo not in inventario:

        codigo_no_existente = True
        inventario[codigo] = (nombre, [precio_inicial])

    return codigo_no_existente

# == actualizar_precio() ==

# Recibe el inventario, el código del producto y el precio a añadir.
# Devuelve False si no encuentra el código y True si lo encuentra

def actualizar_precio(inventario, codigo, nuevo_precio):

    codigo_no_existente = False

    # Si encuentra el producto en el inventario, agrega el precio a la lista de precios

    if codigo in inventario:

        codigo_no_existente = True
        inventario[codigo][1].append(nuevo_precio)

    return codigo_no_existente

# == obtener_producto() ==

# Recibe el inventario y el código del producto. 
# Devuelve una cadena del producto formateado

def obtener_producto(inventario, codigo):

    # Si encuentra el código, crea la cadena

    if codigo in inventario:

        producto = inventario[codigo]
        cadena_producto = f'PRODUCTO: {producto[0]} | PRECIO ACTUAL: {producto[1][-1]}]'

    else:
        cadena_producto = ''

    return cadena_producto

# == analizar_precios_producto() ==

# Recibe el inventario y el código del producto
# Devuelve la lista de precios ordenada de menor a mayor

def analizar_precios_producto(inventario, codigo):

    lista_precios = []

    # Si encuentra el código crea la lista de precios ordenada
    
    if codigo in inventario:
        lista_precios = sorted(inventario[codigo][1])
    
    return lista_precios