from collections.abc import Callable

from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.restaurante import Restaurante


OPCIONES_MENU: tuple[str, ...] = (
    "Registrar producto",
    "Buscar producto",
    "Actualizar producto",
    "Eliminar producto",
    "Listar productos",
    "Registrar usuario",
    "Listar usuarios",
    "Mostrar categorías",
    "Salir",
)


def mostrar_menu() -> None:
    print("\n" + "=" * 40)
    print("        SISTEMA DE RESTAURANTE")
    print("=" * 40)
    for numero, opcion in enumerate(OPCIONES_MENU, start=1):
        print(f"{numero}. {opcion}")


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


def solicitar_correo() -> str:
    while True:
        correo = solicitar_texto("Correo: ")
        if "@" in correo and "." in correo.split("@")[-1]:
            return correo
        print("Ingrese un correo válido, por ejemplo: nombre@correo.com")


def registrar_producto(restaurante: Restaurante) -> None:
    print("\n--- Registrar producto ---")
    codigo = solicitar_texto("Código: ")
    nombre = solicitar_texto("Nombre: ")
    categoria = solicitar_texto("Categoría: ")
    precio = solicitar_precio()
    producto = Producto(codigo, nombre, categoria, precio)
    _, mensaje = restaurante.registrar_producto(producto)
    print(mensaje)


def buscar_producto(restaurante: Restaurante) -> None:
    print("\n--- Buscar producto ---")
    codigo = solicitar_texto("Código del producto: ")
    producto = restaurante.buscar_producto(codigo)
    if producto is None:
        print("No se encontró un producto con ese código.")
        return
    print(producto.mostrar_informacion())


def actualizar_producto(restaurante: Restaurante) -> None:
    print("\n--- Actualizar producto ---")
    codigo = solicitar_texto("Código del producto: ")
    if restaurante.buscar_producto(codigo) is None:
        print("No se encontró un producto con ese código.")
        return
    nuevo_nombre = solicitar_texto("Nuevo nombre: ")
    nueva_categoria = solicitar_texto("Nueva categoría: ")
    nuevo_precio = solicitar_precio()
    _, mensaje = restaurante.actualizar_producto(
        codigo, nuevo_nombre, nueva_categoria, nuevo_precio
    )
    print(mensaje)


def eliminar_producto(restaurante: Restaurante) -> None:
    print("\n--- Eliminar producto ---")
    codigo = solicitar_texto("Código del producto: ")
    _, mensaje = restaurante.eliminar_producto(codigo)
    print(mensaje)


def listar_productos(restaurante: Restaurante) -> None:
    print("\n--- Lista de productos ---")
    productos = restaurante.listar_productos()
    if not productos:
        print("No hay productos registrados.")
        return
    for numero, informacion in enumerate(productos, start=1):
        print(f"{numero}. {informacion}")


def registrar_usuario(restaurante: Restaurante) -> None:
    print("\n--- Registrar usuario ---")
    identificacion = solicitar_texto("Identificación: ")
    nombre = solicitar_texto("Nombre: ")
    correo = solicitar_correo()
    usuario = Usuario(identificacion, nombre, correo)
    _, mensaje = restaurante.registrar_usuario(usuario)
    print(mensaje)


def listar_usuarios(restaurante: Restaurante) -> None:
    print("\n--- Lista de usuarios ---")
    usuarios = restaurante.listar_usuarios()
    if not usuarios:
        print("No hay usuarios registrados.")
        return
    for numero, informacion in enumerate(usuarios, start=1):
        print(f"{numero}. {informacion}")


def mostrar_categorias(restaurante: Restaurante) -> None:
    print("\n--- Categorías únicas ---")
    categorias = restaurante.obtener_categorias()
    if not categorias:
        print("No hay categorías registradas.")
        return
    for categoria in sorted(categorias):
        print(f"- {categoria}")


def main() -> None:
    restaurante = Restaurante()
    acciones: dict[str, Callable[[Restaurante], None]] = {
        "1": registrar_producto,
        "2": buscar_producto,
        "3": actualizar_producto,
        "4": eliminar_producto,
        "5": listar_productos,
        "6": registrar_usuario,
        "7": listar_usuarios,
        "8": mostrar_categorias,
    }
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "9":
            print("Gracias por utilizar el sistema.")
            break
        accion = acciones.get(opcion)
        if accion is None:
            print("Opción no válida. Intente nuevamente.")
            continue
        accion(restaurante)


if __name__ == "__main__":
    main()
