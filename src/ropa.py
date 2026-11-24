# Importamos la clase abstracta Producto.
from producto import Producto


# Clase Ropa que hereda los atributos y métodos de Producto.
class Ropa(Producto):

    # Constructor que inicializa los atributos heredados y los propios.
    def __init__(self, id_producto, nombre, precio, cantidad, talla, material):

        # Llamamos al constructor de la clase padre para inicializar
        # los atributos comunes del producto.
        super().__init__(id_producto, nombre, precio, cantidad)

        # Atributos específicos de las prendas de vestir.
        self.talla = talla
        self.material = material

    # Implementamos el método abstracto para calcular el valor del inventario.
    def calcular_valor_inventario(self):
        return self.precio * self.cantidad

    # Sobrescribimos el método para mostrar información de la prenda.
    def mostrar_informacion(self):
        print(f"ID: {self.id_producto}")
        print(f"Nombre: {self.nombre}")
        print(f"Precio: ${self.precio:.2f}")
        print(f"Cantidad disponible: {self.cantidad}")
        print(f"Talla: {self.talla}")
        print(f"Material: {self.material}")
        print(f"Valor del inventario: ${self.calcular_valor_inventario():.2f}")
