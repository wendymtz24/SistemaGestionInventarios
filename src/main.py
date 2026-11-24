
# Importamos las tres clases derivadas del proyecto.
from electronico import Electronico
from alimento import Alimento
from ropa import Ropa

# Importamos Producto para realizar pruebas de la clase abstracta.
from producto import Producto

# Función principal que ejecuta el sistema de gestión de inventarios.
def main():

    # Creamos un objeto de la clase Electronico.
    producto1 = Electronico(
        1, "Laptop", 12500.00, 5, 24
    )

    # Creamos un objeto de la clase Alimento.
    producto2 = Alimento(
        2, "Leche", 28.50, 20, "15/12/2026"
    )

    # Creamos un objeto de la clase Ropa.
    producto3 = Ropa(
        3, "Playera", 199.00, 10, "M", "Algodón"
    )

    # Prueba 1: verificamos el cálculo del inventario.
    assert producto1.calcular_valor_inventario() == 62500.00
    assert producto2.calcular_valor_inventario() == 570.00
    assert producto3.calcular_valor_inventario() == 1990.00

    print("\nPRUEBA 1: Cálculos del inventario correctos.")
    
    
    # Prueba 2: verificamos los atributos específicos de cada clase.
    assert producto1.garantia_meses == 24
    assert producto2.fecha_caducidad == "15/12/2026"
    assert producto3.talla == "M"
    assert producto3.material == "Algodón"

    print("PRUEBA 2: Atributos específicos correctos.")

   
    # Prueba 3: verificamos que Producto sea una clase abstracta.
    try:
        Producto(4, "Producto de prueba", 100.00, 2)

    except TypeError:
        print("PRUEBA 3: La clase abstracta Producto no permite crear objetos directamente.")

    else:
        raise AssertionError("Error: se pudo instanciar la clase abstracta Producto.")

   
    # Almacenamos los diferentes objetos en una misma lista.
    inventario = [producto1, producto2, producto3]

    # Mostramos el título del sistema.
    print("=" * 50)
    print("       SISTEMA DE GESTIÓN DE INVENTARIOS")
    print("=" * 50)

    # Recorremos la lista y llamamos al mismo método
    # para cada objeto, demostrando el polimorfismo.
    for producto in inventario:
        print("\n--- INFORMACIÓN DEL PRODUCTO ---")
        producto.mostrar_informacion()

    # Calculamos el valor total de todos los productos.
    valor_total = sum(
        producto.calcular_valor_inventario()
        for producto in inventario
    )

    # Mostramos el valor total del inventario.
    print("\n" + "=" * 50)
    print(f"VALOR TOTAL DEL INVENTARIO: ${valor_total:,.2f}")
    print("=" * 50)


# Ejecutamos la función principal cuando se inicia este archivo.
if __name__ == "__main__":
    main()
