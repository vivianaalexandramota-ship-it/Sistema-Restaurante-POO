from modelos.producto import Producto
from modelos.usuario import Usuario


class Restaurante:
    """Administra las colecciones y operaciones del sistema."""

    def __init__(self) -> None:
        self._productos: list[Producto] = []
        self._usuarios: list[Usuario] = []

    def registrar_producto(self, producto: Producto) -> tuple[bool, str]:
        if self._existe_codigo_producto(producto.codigo):
            return False, "Ya existe un producto con ese código."
        self._productos.append(producto)
        return True, "Producto registrado correctamente."

    def buscar_producto(self, codigo: str) -> Producto | None:
        codigo_buscado = codigo.strip().lower()
        for producto in self._productos:
            if producto.codigo.lower() == codigo_buscado:
                return producto
        return None

    def actualizar_producto(
        self,
        codigo: str,
        nuevo_nombre: str,
        nueva_categoria: str,
        nuevo_precio: float,
    ) -> tuple[bool, str]:
        producto = self.buscar_producto(codigo)
        if producto is None:
            return False, "No se encontró un producto con ese código."
        producto.nombre = nuevo_nombre.strip()
        producto.categoria = nueva_categoria.strip()
        producto.precio = nuevo_precio
        return True, "Producto actualizado correctamente."

    def eliminar_producto(self, codigo: str) -> tuple[bool, str]:
        producto = self.buscar_producto(codigo)
        if producto is None:
            return False, "No se encontró un producto con ese código."
        self._productos.remove(producto)
        return True, "Producto eliminado correctamente."

    def listar_productos(self) -> list[str]:
        return [producto.mostrar_informacion() for producto in self._productos]

    def obtener_categorias(self) -> set[str]:
        return {producto.categoria for producto in self._productos}

    def registrar_usuario(self, usuario: Usuario) -> tuple[bool, str]:
        if self._existe_identificacion_usuario(usuario.identificacion):
            return False, "Ya existe un usuario con esa identificación."
        self._usuarios.append(usuario)
        return True, "Usuario registrado correctamente."

    def listar_usuarios(self) -> list[str]:
        return [usuario.mostrar_informacion() for usuario in self._usuarios]

    def _existe_codigo_producto(self, codigo: str) -> bool:
        return self.buscar_producto(codigo) is not None

    def _existe_identificacion_usuario(self, identificacion: str) -> bool:
        identificacion_buscada = identificacion.strip().lower()
        return any(
            usuario.identificacion.lower() == identificacion_buscada
            for usuario in self._usuarios
        )
