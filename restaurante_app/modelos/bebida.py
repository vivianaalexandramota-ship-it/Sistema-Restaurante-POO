from modelos.producto import Producto


class Bebida(Producto):
    """Representa una bebida, que es un tipo específico de Producto."""

    def __init__(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: float,
        tamano: str,
        tipo_envase: str,
    ) -> None:
        super().__init__(codigo, nombre, categoria, precio)
        self.tamano = tamano.strip()
        self.tipo_envase = tipo_envase.strip()

    def mostrar_informacion(self) -> str:
        return (
            f"{super().mostrar_informacion()} | "
            f"Tamaño: {self.tamano} | "
            f"Envase: {self.tipo_envase}"
        )
