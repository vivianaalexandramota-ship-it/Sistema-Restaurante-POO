from modelos.bebida import Bebida
from modelos.cliente import Cliente
from modelos.producto import Producto
from servicios.restaurante import Restaurante


def mostrar_menu() -> None:
    print("\n" + "=" * 40)
    print("        SISTEMA DE RESTAURANTE")
    print("=" * 40)
    print("1. Registrar producto")
    print("2. Registrar bebida")
    print("3. Registrar cliente")
    print("-" * 40)
    print("4. Listar productos")
    print("5. Listar clientes")
    print("-" * 40)
    print("6. Salir")


def solicitar_texto(mensaje: str) -> str:
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("El campo no puede quedar vacío.")


def solicitar_precio() -> float:
    while True:
        entrada = input("Precio: ").strip()
        try:
            precio = float(entrada)
            if precio > 0:
                return precio
            print("El precio debe ser mayor que cero.")
        except ValueError:
            print("Ingrese un precio numérico válido.")


def registrar_producto(restaurante: Restaurante) -> None:
    print("\n--- Registrar producto ---")
    codigo = solicitar_texto("Código: ")
    nombre = solicitar_texto("Nombre: ")
    categoria = solicitar_texto("Categoría: ")
    precio = solicitar_precio()

    producto = Producto(codigo, nombre, categoria, precio)
    _, mensaje = restaurante.registrar_producto(producto)
    print(mensaje)


def registrar_bebida(restaurante: Restaurante) -> None:
    print("\n--- Registrar bebida ---")
    codigo = solicitar_texto("Código: ")
    nombre = solicitar_texto("Nombre: ")
    categoria = solicitar_texto("Categoría: ")
    precio = solicitar_precio()
    tamano = solicitar_texto("Tamaño o presentación: ")
    tipo_envase = solicitar_texto("Tipo de envase: ")

    bebida = Bebida(codigo, nombre, categoria, precio, tamano, tipo_envase)
    _, mensaje = restaurante.registrar_producto(bebida)
    print(mensaje)


def registrar_cliente(restaurante: Restaurante) -> None:
    print("\n--- Registrar cliente ---")
    identificacion = solicitar_texto("Identificación: ")
    nombre = solicitar_texto("Nombre: ")
    correo = solicitar_texto("Correo: ")

    cliente = Cliente(identificacion, nombre, correo)
    _, mensaje = restaurante.registrar_cliente(cliente)
    print(mensaje)


def listar_productos(restaurante: Restaurante) -> None:
    print("\n--- Lista de productos ---")
    productos = restaurante.listar_productos()

    if not productos:
        print("No hay productos registrados.")
        return

    for numero, informacion in enumerate(productos, start=1):
        print(f"{numero}. {informacion}")


def listar_clientes(restaurante: Restaurante) -> None:
    print("\n--- Lista de clientes ---")
    clientes = restaurante.listar_clientes()

    if not clientes:
        print("No hay clientes registrados.")
        return

    for numero, informacion in enumerate(clientes, start=1):
        print(f"{numero}. {informacion}")


def main() -> None:
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
            print("Gracias por utilizar el sistema.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()
