# Restaurante App - Semana 9

## Estudiante

Viviana Mota Alzamora

## Descripción

Sistema de consola en Python para administrar productos y usuarios de un restaurante. Permite registrar, buscar, actualizar, eliminar y listar productos; registrar y listar usuarios; y mostrar categorías únicas.

## Estructura

```text
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
└── main.py
README.md
```

## Responsabilidades

- `Producto`: representa un producto mediante código, nombre, categoría y precio.
- `Usuario`: representa una persona mediante identificación, nombre y correo.
- `Restaurante`: administra las colecciones y las operaciones del sistema.
- `main.py`: presenta el menú, solicita los datos y llama al servicio.

## Estructuras de datos

- `list`: almacena las colecciones dinámicas de productos y usuarios.
- `tuple`: mantiene estables las opciones de `OPCIONES_MENU`.
- `dict`: relaciona los números del menú con las funciones correspondientes.
- `set`: obtiene las categorías de productos sin duplicados.

Las cuatro estructuras cumplen una función real dentro del programa.

## Validaciones

- Campos de texto obligatorios.
- Precio numérico mayor que cero.
- Formato básico de correo electrónico.
- Códigos de productos no duplicados.
- Identificaciones de usuarios no duplicadas.
- Opciones incorrectas del menú controladas.
- Operaciones sobre productos inexistentes controladas.

## Ejecución

Desde la carpeta `restaurante_app`, ejecute:

```bash
python main.py
```

## Reflexión

Seleccionar una estructura adecuada permite representar mejor cada necesidad. Las listas facilitan administrar colecciones que cambian; las tuplas conservan información estable; los diccionarios relacionan claves con acciones; y los conjuntos eliminan duplicados. Esto mejora la claridad y el mantenimiento del sistema.
