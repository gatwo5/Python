from abc import ABC, abstractmethod

# === CLASE PRODUCTO ===

class Producto(ABC):

    def __init__(self, nombre):
         
         # --- Constructor ---

         self._nombre = nombre
         self._precios = [] # Crea la lista ya vacía al instanciar
    
    # --- GETTERES Y SETTERS ---

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    @property
    def precios(self):
        return self._precios[-1] # Devuelve el último precio
    
    # --- MÉTODOS DE INSTANCIA ---
    
    # agregar_precio()
    # Recibe el precio para insertarlo

    def agregar_precio(self, precio):

        # En caso de ser negativo, rechaza el valor

        if(precio < 0):
            print('No puede haber precios negativos')
        else:
            self._precios.append(precio)
        
    # calcular_preco_final()
    # Método abstracto a modo de plantilla

    @abstractmethod
    def calcular_precio_final(self):
        pass

# === CLASE DiscoDuro ===

class DiscoDuro(Producto):

    # --- CONSTRUCTOR ---

    def __init__(self, nombre, tipo):
        super().__init__(nombre)
        self._tipo = tipo

    # --- MÉTODOS DE INSTANCIA ---
    # calcular_precio_final()
    # Devuelve el precio final calculado

    def calcular_precio_final(self):
        precio = 0

        # En caso de ser SSD +20%

        if self._tipo == "SSD":
            precio = self.precios + self.precios * 0.20
        else:
            precio = self.precios

        return precio
            
    # Sobrescribir __str__

    def __str__(self):
        return f"Disco duro | Nombre: {self._nombre} | Tipo: {self._tipo}"
    
# === CLASE Memoria ===

class Memoria(Producto):

    # --- CONSTRUCTOR ---

    def __init__(self, nombre, capacidad):
        super().__init__(nombre)
        self._capacidad = capacidad

    # --- MÉTODOS DE INSTANCIA ---

    # calcular_precio_final()
    # Devuelve el precio final calculado

    def calcular_precio_final(self):
        precio = 0

        # En caso de tener una capacidad de 16GB +50%

        if self._capacidad == 16:
            precio = self.precios + self.precios * 0.50
        else:
            precio = self.precios

        return precio
    
    # Sobrescribir __str__

    def __str__(self):
        return f"Memoria | Nombre: {self._nombre} | Capacidad: {self._capacidad}"