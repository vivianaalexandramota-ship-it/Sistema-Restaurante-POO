class Cliente:
    """Representa únicamente la información de un cliente."""

    def __init__(self, identificacion: str, nombre: str, correo: str) -> None:
        self.identificacion = identificacion.strip()
        self.nombre = nombre.strip()
        self.correo = correo.strip()

    def mostrar_informacion(self) -> str:
        return (
            f"Identificación: {self.identificacion} | "
            f"Nombre: {self.nombre} | "
            f"Correo: {self.correo}"
        )
