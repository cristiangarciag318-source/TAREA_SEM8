# Taller Prácitco — Semana 8

**Estudiante:** Cristian Omar García Aguilar  
**Asignatura:** Programación Orientada a Objetos  
**Semana:** 8 — Organización modular de un sistema orientado a objetos en Python

---

## Descripción del sistema

Proyecto Python que modela la gestión básica de un restaurante usando programación orientada a objetos. Permite registrar y listar productos, bebidas y clientes desde consola. Las categorías de producto están restringidas a valores predefinidos y el tamaño de las bebidas acepta tanto formatos descriptivos como unidades de medida.

---

## Estructura del proyecto

```
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

---

## Responsabilidad de cada clase

| Clase / Archivo | Responsabilidad |
|---|---|
| `Producto` | Clase base del catálogo. Valida que la categoría pertenezca a un conjunto predefinido de valores. |
| `Bebida` | Hereda de `Producto`. El tamaño acepta valores descriptivos (pequeño, mediano, grande) o con unidad (ml, L). |
| `Cliente` | Entidad independiente. El nombre se capitaliza automáticamente y debe incluir al menos nombre y apellido. |
| `Restaurante` | Administra productos y clientes, verifica duplicados y expone listados sin distinguir tipos concretos. |
| `main.py` | Interacción por consola: muestra las opciones disponibles para categoría y tamaño antes de solicitar datos. |

---

## Relación entre Producto y Bebida

`Bebida` hereda de `Producto` porque una bebida es un tipo de producto del restaurante con atributos adicionales. El servicio almacena ambos en `_productos` y llama a `mostrar_informacion()` de forma uniforme sobre cada elemento, sin condiciones que distingan el tipo.

---

## Principios SOLID aplicados

### S — Responsabilidad única (SRP)

Cada clase tiene una sola razón para cambiar. `Producto` cambia si se modifica la estructura del catálogo o las categorías válidas. `Bebida` cambia si se modifica lo que define a una bebida. `Cliente` cambia si cambia la información del cliente. `Restaurante` cambia si cambia la lógica de administración. `main.py` cambia si cambia la interacción con el usuario.

### O — Abierto/Cerrado (OCP)

`Bebida` amplía el sistema con tamaño y tipo de envase sin modificar `Producto` ni `Restaurante`. Agregar una clase `Postre` con atributos propios seguiría el mismo patrón sin alterar el código existente.

### L — Sustitución de Liskov (LSP)

Un objeto `Bebida` funciona correctamente en cualquier contexto donde se espera un `Producto`. El servicio registra y lista ambos tipos de forma uniforme mediante `mostrar_informacion()`, sin verificar el tipo concreto de cada objeto en ningún momento.

---

## Instrucciones de ejecución

1. Descargar o clonar el repositorio.
2. Desde la carpeta raíz del proyecto ejecutar:

```bash
python restaurante_app/main.py
```

3. Al registrar productos y bebidas, el sistema indica las opciones válidas de categoría y tamaño.

---

## Reflexión

Un proyecto bien organizado no es aquel que funciona hoy, sino aquel que puede mantenerse y crecer sin convertirse en un problema. Separar responsabilidades, aplicar herencia solo cuando existe una relación real entre clases y mantener la lógica de negocio fuera de la interfaz de usuario son hábitos que valen la pena desarrollar desde los primeros proyectos.
