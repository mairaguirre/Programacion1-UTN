# productos.py

ARCHIVO = "productos.txt"
# ----------------------------------------------------------
# 1. Creo el archivo inicial con 3 productos (solo si no existe)

def crear_archivo_inicial():
    try:
        # "x" falla si el archivo ya existe, así evitamos sobrescribir
        # datos que ya estén guardados
        with open(ARCHIVO, "x") as f:
            f.write("Lapicera,120.5,30\n")
            f.write("Cuaderno,350.0,15\n")
            f.write("Mochila,8500.0,5\n")
        print(f"Archivo '{ARCHIVO}' creado con productos iniciales.\n")
    except FileExistsError:
        # Si ya existe, no hacemos nada (no se pisa)
        print(f"El archivo '{ARCHIVO}' ya existe, no se modifica.\n")


# ----------------------------------------------------------
# 2 y 4. Leer el archivo y cargar los datos en una lista de diccionarios

def cargar_productos():
    productos = []
    try:
        with open(ARCHIVO, "r") as f:
            for linea in f:
                linea = linea.strip()
                if linea == "":          # ignoro líneas vacías
                    continue
                nombre, precio, cantidad = linea.split(",")
                producto = {
                    "nombre": nombre,
                    "precio": float(precio),
                    "cantidad": int(cantidad)
                }
                productos.append(producto)
    except FileNotFoundError:
        print(f"No se encontró el archivo '{ARCHIVO}'.")
    return productos


def mostrar_productos(productos):
    if not productos:
        print("No hay productos para mostrar.")
        return
    print("LISTADO DE PRODUCTOS")
    for p in productos:
        print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")
    print()

# ----------------------------------------------------------
# 3. Agrego un producto nuevo

def agregar_producto(productos):
    print("--- AGREGAR NUEVO PRODUCTO ---")
    nombre = input("Nombre del producto: ").strip()

    # Valido que precio y cantidad sean numéricos
    while True:
        try:
            precio = float(input("Precio: ").strip())
            break
        except ValueError:
            print("Precio inválido, ingresá un número (ej: 150.5).")

    while True:
        try:
            cantidad = int(input("Cantidad: ").strip())
            break
        except ValueError:
            print("Cantidad inválida, ingresá un número entero.")

    nuevo = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    productos.append(nuevo)  # lo agrego en memoria, a la lista
    print(f"Producto '{nombre}' agregado correctamente.\n")
    return productos

# ----------------------------------------------------------
# 5. Busco un producto por nombre

def buscar_producto(productos):
    nombre_buscado = input("Ingresá el nombre del producto a buscar: ").strip().lower()

    for p in productos:
        if p["nombre"].lower() == nombre_buscado:
            print("--- PRODUCTO ENCONTRADO ---")
            print(f"Nombre: {p['nombre']}")
            print(f"Precio: ${p['precio']}")
            print(f"Cantidad: {p['cantidad']}\n")
            return

    print(f"No se encontró ningún producto llamado '{nombre_buscado}'.\n")

# ----------------------------------------------------------
# 6. Guardo (se sobrescribe) el archivo con la lista actualizada

def guardar_productos(productos):
    with open(ARCHIVO, "w") as f:
        for p in productos:
            f.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")
    print(f"Archivo '{ARCHIVO}' actualizado correctamente.\n")

