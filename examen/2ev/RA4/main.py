from funciones import crear_inventario, agregar_producto, actualizar_precio, obtener_producto, analizar_precios_producto

def main():
    inventario = crear_inventario()

    # Añade dos productos nuevos

    agregar_producto(inventario, "P001", "Móvil", 499.99)
    agregar_producto(inventario, "P002", "PC", 999.99)

    # Intenta añadir un producto duplicado

    agregar_producto(inventario, "P002", "Switch", 549.99)

    # Actualiza el precio de los dos productos

    actualizar_precio(inventario, "P001", 200.50)
    actualizar_precio(inventario, "P002", 1699.99)

    # Muestra un producto

    print(obtener_producto(inventario, "P001"))

    # Analiza el precio de un producto

    print(analizar_precios_producto(inventario, "P001"))


if __name__ == "__main__":
    main()
    