from modelos.cliente import Cliente
from modelos.producto import Producto


class Restaurante:
    """Administra las colecciones y operaciones del sistema."""

    def __init__(self) -> None:
        self._productos: list[Producto] = []
        self._clientes: list[Cliente] = []

    def registrar_producto(self, producto: Producto) -> tuple[bool, str]:
        if self._existe_codigo_producto(producto.codigo):
            return False, "Ya existe un producto con ese código."

        self._productos.append(producto)
        return True, "Producto registrado correctamente."

    def listar_productos(self) -> list[str]:
        return [producto.mostrar_informacion() for producto in self._productos]

    def registrar_cliente(self, cliente: Cliente) -> tuple[bool, str]:
        if self._existe_identificacion_cliente(cliente.identificacion):
            return False, "Ya existe un cliente con esa identificación."

        self._clientes.append(cliente)
        return True, "Cliente registrado correctamente."

    def listar_clientes(self) -> list[str]:
        return [cliente.mostrar_informacion() for cliente in self._clientes]

    def _existe_codigo_producto(self, codigo: str) -> bool:
        codigo_buscado = codigo.strip().lower()
        return any(
            producto.codigo.lower() == codigo_buscado
            for producto in self._productos
        )

    def _existe_identificacion_cliente(self, identificacion: str) -> bool:
        identificacion_buscada = identificacion.strip().lower()
        return any(
            cliente.identificacion.lower() == identificacion_buscada
            for cliente in self._clientes
        )
