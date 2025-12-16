from clases import DiscoDuro, Memoria

def main():
    # Crear objetos

    disco1 = DiscoDuro("Samnsung", "SSD")

    disco1.agregar_precio(200)
    disco1.agregar_precio(400)

    disco2 = DiscoDuro("Sony", "HDD")

    disco2.agregar_precio(100)
    disco2.agregar_precio(300)

    memoria1 = Memoria("Western Digital", 16)

    memoria1.agregar_precio(10)
    memoria1.agregar_precio(20)

    memoria2 = Memoria("HP", 10)

    memoria2.agregar_precio(50)
    memoria2.agregar_precio(40)

    # Meterlos en el inventario

    inventario = [disco1, disco2, memoria1, memoria2]

    # Pruebas
    
    for producto in inventario:

        print(producto)
        print("Precio actual:",producto.precios)
        print("Precio Final calculado:",producto.calcular_precio_final())
        print()

if __name__ == "__main__":
    main()