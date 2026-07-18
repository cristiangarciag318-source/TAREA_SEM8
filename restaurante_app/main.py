from modelos.producto import Producto
from modelos.bebida import Bebida
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


def mostrar_menu() -> None:
    print("\n========================================")
    print("        SISTEMA DE RESTAURANTE")
    print("========================================")
    print("1. Registrar producto")
    print("2. Registrar bebida")
    print("3. Registrar cliente")
    print("----------------------------------------")
    print("4. Listar productos")
    print("5. Listar clientes")
    print("----------------------------------------")
    print("6. Salir")


def registrar_producto(servicio: Restaurante) -> None:
    print("\n-- Registrar Producto --")
    print("Categorias disponibles: Entradas, Platos fuertes, Postres, Bebidas, Acompanantes")
    try:
        codigo = input("Codigo: ")
        nombre = input("Nombre: ")
        categoria = input("Categoria: ")
        precio = float(input("Precio: "))
        producto = Producto(codigo, nombre, categoria, precio)
    except ValueError as error:
        print(f"Error al registrar: {error}")
        return
    if servicio.registrar_producto(producto):
        print("Producto agregado al sistema.")
    else:
        print(f"El codigo '{producto.codigo}' ya existe en el sistema.")


def registrar_bebida(servicio: Restaurante) -> None:
    print("\n-- Registrar Bebida --")
    print("Categorias disponibles: Bebidas")
    print("Tamano: descriptivo (pequeño, mediano, grande) o con unidad (250ml, 1L)")
    try:
        codigo = input("Codigo: ")
        nombre = input("Nombre: ")
        categoria = input("Categoria: ")
        precio = float(input("Precio: "))
        tamano = input("Tamano: ")
        tipo_envase = input("Tipo de envase (ej. botella, vaso, lata): ")
        bebida = Bebida(codigo, nombre, categoria, precio, tamano, tipo_envase)
    except ValueError as error:
        print(f"Error al registrar: {error}")
        return
    if servicio.registrar_producto(bebida):
        print("Bebida agregada al sistema.")
    else:
        print(f"El codigo '{bebida.codigo}' ya existe en el sistema.")


def registrar_cliente(servicio: Restaurante) -> None:
    print("\n-- Registrar Cliente --")
    try:
        identificacion = input("Identificacion: ")
        nombre = input("Nombre completo (nombre y apellido): ")
        correo = input("Correo: ")
        cliente = Cliente(identificacion, nombre, correo)
    except ValueError as error:
        print(f"Error al registrar: {error}")
        return
    if servicio.registrar_cliente(cliente):
        print("Cliente agregado al sistema.")
    else:
        print(f"La identificacion '{cliente.identificacion}' ya existe en el sistema.")


def listar_productos(servicio: Restaurante) -> None:
    print("\n-- Lista de Productos --")
    registros = servicio.listar_productos()
    if not registros:
        print("No existen productos registrados.")
        return
    for registro in registros:
        print(registro)


def listar_clientes(servicio: Restaurante) -> None:
    print("\n-- Lista de Clientes --")
    registros = servicio.listar_clientes()
    if not registros:
        print("No existen clientes registrados.")
        return
    for registro in registros:
        print(registro)


def main() -> None:
    servicio = Restaurante()
    opciones = {
        "1": registrar_producto,
        "2": registrar_bebida,
        "3": registrar_cliente,
        "4": listar_productos,
        "5": listar_clientes,
    }
    while True:
        mostrar_menu()
        opcion = input("\nIngrese una opcion: ").strip()
        if opcion == "6":
            print("\nSaliendo del sistema.")
            break
        accion = opciones.get(opcion)
        if accion:
            accion(servicio)
        else:
            print("Opcion invalida. Ingrese un numero entre 1 y 6.")


if __name__ == "__main__":
    main()
