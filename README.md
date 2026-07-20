# Restaurante App - Semana 8

## Estudiante

Viviana Mota Alzamora

## Descripción

Este proyecto corresponde a la Semana 8 de Programación Orientada a Objetos. El sistema permite registrar productos, bebidas y clientes desde un menú interactivo en consola, además de listar los registros almacenados durante la ejecución.

## Estructura del proyecto

```text
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── bebida.py
│   └── cliente.py
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
└── main.py
README.md
```

## Responsabilidad de cada clase

- `Producto`: representa los datos comunes de los productos.
- `Bebida`: hereda de `Producto` y agrega tamaño y tipo de envase.
- `Cliente`: representa únicamente la información de un cliente.
- `Restaurante`: administra las listas, registra información y evita duplicados.
- `main.py`: coordina la interacción con el usuario mediante consola.

## Principios SOLID aplicados

### Responsabilidad única (SRP)

Cada clase cumple una tarea específica. Las entidades representan información, el servicio administra las colecciones y `main.py` se encarga de la interacción.

### Abierto/cerrado (OCP)

La clase `Bebida` amplía el sistema mediante herencia sin modificar la lógica general del servicio.

### Sustitución de Liskov (LSP)

Los objetos `Producto` y `Bebida` se almacenan en una misma lista y responden al método `mostrar_informacion()` sin condiciones específicas.

## Validaciones

El sistema valida campos vacíos, precios inválidos, códigos de productos repetidos e identificaciones de clientes duplicadas.

## Ejecución

Desde la carpeta `restaurante_app`, ejecute:

```bash
python main.py
```

## Reflexión

Aplicar los principios SOLID ayuda a mantener el proyecto organizado y facilita la incorporación de nuevas clases sin alterar innecesariamente el código existente.
