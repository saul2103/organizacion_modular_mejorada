from modelos.producto import Producto
from modelos.bebida import Bebida
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

def mostrar_menu():
    """Menu principal"""
    print("\n" + "=" * 40)
    print("    RESTAURANTE RECETAS DE MI SIERRA")
    print("=" * 40)
    print("1. Registrar producto")
    print("2. Registrar bebida")
    print("3. Registrar cliente")
    print("-" * 40)
    print("4. Listar productos")
    print("5. Listar clientes")
    print("-" * 40)
    print("6. Salir")
    print("=" * 40)

def registrar_producto(restaurante: Restaurante):
    """Registro de nuevo producto"""
    
    try:
        codigo = Restaurante.validar_codigo(input("Código: "))
        nombre = Restaurante.validar_nombre(input("Nombre: "))
        categoria = Restaurante.validar_categoria(input("Categoría: "))
        precio = Restaurante.validar_precio(input("Precio: "))
        producto = Producto(codigo, nombre, categoria, precio)
        if restaurante.registrar_producto(producto):
            print(" Producto registrado exitosamente.")
        else:
            print(" Error: Ya existe un producto con ese código.")
    except ValueError as e:
        print(f" Error: {e}")

def registrar_bebida(restaurante: Restaurante):
    """Registro de nueva bebida"""
    try:
        codigo = Restaurante.validar_codigo(input("Código: "))
        nombre = Restaurante.validar_nombre(input("Nombre: "))
        categoria = Restaurante.validar_categoria(input("Categoría: "))
        precio = Restaurante.validar_precio(input("Precio: "))
        tamanio = Restaurante.validar_tamanio(input("Tamaño (ej: 500ml): "))
        tipo_envase = Restaurante.validar_tipo_envase(input("Tipo de envase: "))
        bebida = Bebida(codigo, nombre, categoria, precio, tamanio, tipo_envase)
        if restaurante.registrar_producto(bebida):
            print(" Bebida registrada exitosamente.")
        else:
            print(" Error: Ya existe un producto con ese código.")
    except ValueError as e:
        print(f" Error: {e}")

def registrar_cliente(restaurante: Restaurante):
    """Registro de nuevo cliente"""
    try:
        identificacion = Restaurante.validar_identificacion(input("Identificación: "))
        nombre = Restaurante.validar_nombre(input("Nombre: "))
        correo = Restaurante.validar_correo(input("Correo: "))
        cliente = Cliente(identificacion, nombre, correo)
        if restaurante.registrar_cliente(cliente):
            print(" Cliente registrado exitosamente.")
        else:
            print(" Error: Ya existe un cliente con esa identificación.")
    except ValueError as e:
        print(f" Error: {e}")

def listar_productos(restaurante: Restaurante):
    """Listar todos los productos registrados"""
    productos = restaurante.listar_productos()
    if not productos:
        print("No hay productos registrados.")
    else:
        print("\n--- LISTA DE PRODUCTOS ---")
        for producto_info in productos:
            print(producto_info)

def listar_clientes(restaurante: Restaurante):
    """Listar todos los clientes registrados"""
    clientes = restaurante.listar_clientes()
    if not clientes:
        print("No hay clientes registrados.")
    else:
        print("\n--- LISTA DE CLIENTES ---")
        for cliente_info in clientes:
            print(cliente_info)

def main():
    """Función principal del programa"""
    restaurante = Restaurante()
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            registrar_producto(restaurante)
        elif opcion == "2":
            registrar_bebida(restaurante)
        elif opcion == "3":
            registrar_cliente(restaurante)
        elif opcion == "4":
            listar_productos(restaurante)
        elif opcion == "5":
            listar_clientes(restaurante)
        elif opcion == "6":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()