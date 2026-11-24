
# Importamos ABC y abstractmethod para crear una clase abstracta.
from abc import ABC, abstractmethod


# Clase abstracta que establece la estructura general de los productos.
class Producto(ABC):

    # Constructor: inicializa los atributos comunes de cada producto.
    def __init__(self, id_producto, nombre, precio, cantidad):
        self.id_producto = id_producto  # Identificador único del producto.
        self.nombre = nombre            # Nombre del producto.
        self.precio = precio            # Precio unitario.
        self.cantidad = cantidad        # Unidades disponibles en inventario.

    # Método abstracto para calcular el valor total del inventario.
    # Las clases derivadas deberán implementar este método.
    @abstractmethod
    def calcular_valor_inventario(self):
        pass

    # Método abstracto para mostrar la información del producto.
    # Cada clase derivada definirá cómo presentar sus datos.
    @abstractmethod
    def mostrar_informacion(self):
        pass
