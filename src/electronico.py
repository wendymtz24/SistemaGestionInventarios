
# Importamos la clase abstracta Producto.
from producto import Producto


# Clase Electronico que hereda los atributos y métodos de Producto.
class Electronico(Producto):

    # Constructor que inicializa los atributos heredados y uno propio.
    def __init__(self, id_producto, nombre, precio, cantidad, garantia_meses):

        # Llamamos al constructor de la clase padre para inicializar
        # los atributos comunes del producto.
        super().__init__(id_producto, nombre, precio, cantidad)

        # Atributo específico que indica la garantía del producto en meses.
        self.garantia_meses = garantia_meses

    # Implementamos el método abstracto para calcular el valor del inventario.
    def calcular_valor_inventario(self):
        return self.precio * self.cantidad

    # Sobrescribimos el método para mostrar información del producto electrónico.
    def mostrar_informacion(self):
        print(f"ID: {self.id_producto}")
        print(f"Nombre: {self.nombre}")
        print(f"Precio: ${self.precio:.2f}")
        print(f"Cantidad disponible: {self.cantidad}")
        print(f"Garantía: {self.garantia_meses} meses")
        print(f"Valor del inventario: ${self.calcular_valor_inventario():.2f}")
