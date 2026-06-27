# Programa principal

import productos as p

def main():
    p.crear_archivo_inicial()

    productos = p.cargar_productos()
    p.mostrar_productos(productos)

    productos = p.agregar_producto(productos)
    p.mostrar_productos(productos)

    p.buscar_producto(productos)

    p.guardar_productos(productos)


if __name__ == "__main__":
    main()