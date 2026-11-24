
# Importamos la clase abstracta Producto.
from producto import Producto


# Clase Alimento que hereda los atributos y métodos de Producto.
class Alimento(Producto):

    # Constructor que inicializa los atributos heredados y uno propio.
    def __init__(self, id_producto, nombre, precio, cantidad, fecha_caducidad):

        # Llamamos al constructor de la clase padre para inicializar
        # los atributos comunes del producto.
        super().__init__(id_producto, nombre, precio, cantidad)

        # Atributo específico que indica la fecha de caducidad del alimento.
        self.fecha_caducidad = fecha_caducidad

    # Implementamos el método abstracto para calcular el valor del inventario.
    def calcular_valor_inventario(self):
        return self.precio * self.cantidad

    # Sobrescribimos el método para mostrar información del alimento.
    def mostrar_informacion(self):
        print(f"ID: {self.id_producto}")
        print(f"Nombre: {self.nombre}")
        print(f"Precio: ${self.precio:.2f}")
        print(f"Cantidad disponible: {self.cantidad}")
        print(f"Fecha de caducidad: {self.fecha_caducidad}")
        print(f"Valor del inventario: ${self.calcular_valor_inventario():.2f}")
