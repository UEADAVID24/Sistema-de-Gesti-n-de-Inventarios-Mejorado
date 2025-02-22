import os
import json


class Inventario:
    ARCHIVO_INVENTARIO = "inventario.txt"

    def __init__(self):
        self.productos = {}
        self.cargar_inventario()

    def cargar_inventario(self):
        """Carga el inventario desde un archivo si existe."""
        try:
            if os.path.exists(self.ARCHIVO_INVENTARIO):
                with open(self.ARCHIVO_INVENTARIO, "r") as archivo:
                    self.productos = json.load(archivo)
                    print("Inventario cargado exitosamente.")
            else:
                print("No se encontró un archivo de inventario, se creará uno nuevo.")
                self.guardar_inventario()
        except (FileNotFoundError, json.JSONDecodeError):
            print("Error al leer el archivo de inventario. Creando un archivo nuevo...")
            self.guardar_inventario()
        except PermissionError:
            print("Error: No tienes permisos para acceder al archivo de inventario.")

    def guardar_inventario(self):
        """Guarda el inventario en un archivo."""
        try:
            with open(self.ARCHIVO_INVENTARIO, "w") as archivo:
                json.dump(self.productos, archivo, indent=4)
                print("Inventario guardado exitosamente.")
        except PermissionError:
            print("Error: No tienes permisos para escribir en el archivo de inventario.")

    def agregar_producto(self, codigo, nombre, cantidad, precio):
        """Agrega un producto al inventario y guarda los cambios."""
        self.productos[codigo] = {"nombre": nombre, "cantidad": cantidad, "precio": precio}
        self.guardar_inventario()
        print(f"Producto '{nombre}' agregado exitosamente.")

    def actualizar_producto(self, codigo, cantidad=None, precio=None):
        """Actualiza la cantidad y/o precio de un producto existente."""
        if codigo in self.productos:
            if cantidad is not None:
                self.productos[codigo]["cantidad"] = cantidad
            if precio is not None:
                self.productos[codigo]["precio"] = precio
            self.guardar_inventario()
            print(f"Producto '{self.productos[codigo]['nombre']}' actualizado correctamente.")
        else:
            print("Error: Producto no encontrado.")

    def eliminar_producto(self, codigo):
        """Elimina un producto del inventario."""
        if codigo in self.productos:
            del self.productos[codigo]
            self.guardar_inventario()
            print("Producto eliminado exitosamente.")
        else:
            print("Error: Producto no encontrado.")

    def mostrar_inventario(self):
        """Muestra todos los productos en el inventario."""
        if not self.productos:
            print("El inventario está vacío.")
        else:
            print("Inventario actual:")
            for codigo, datos in self.productos.items():
                print(
                    f"Código: {codigo} | Nombre: {datos['nombre']} | Cantidad: {datos['cantidad']} | Precio: ${datos['precio']}")


# Ejemplo de uso
if __name__ == "__main__":
    inventario = Inventario()
    while True:
        print("\nOpciones:")
        print("1. Agregar producto")
        print("2. Actualizar producto")
        print("3. Eliminar producto")
        print("4. Mostrar inventario")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            codigo = input("Ingrese código del producto: ")
            nombre = input("Ingrese nombre del producto: ")
            cantidad = int(input("Ingrese cantidad: "))
            precio = float(input("Ingrese precio: "))
            inventario.agregar_producto(codigo, nombre, cantidad, precio)
        elif opcion == "2":
            codigo = input("Ingrese código del producto a actualizar: ")
            cantidad = input("Ingrese nueva cantidad (deje en blanco para no modificar): ")
            precio = input("Ingrese nuevo precio (deje en blanco para no modificar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(codigo, cantidad, precio)
        elif opcion == "3":
            codigo = input("Ingrese código del producto a eliminar: ")
            inventario.eliminar_producto(codigo)
        elif opcion == "4":
            inventario.mostrar_inventario()
        elif opcion == "5":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")
