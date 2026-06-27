# Menú principal
# ============================================================
import recursividad as r

def main():
    opciones = {
        "1": ("Factorial", r.mostrar_factoriales),
        "2": ("Fibonacci", r.mostrar_fibonacci),
        "3": ("Potencia", r.probar_potencia),
        "4": ("Decimal a binario", r.probar_decimal_a_binario),
        "5": ("Palíndromo", r.probar_palindromo),
        "6": ("Suma de dígitos", r.probar_suma_digitos),
        "7": ("Contar bloques (pirámide)", r.probar_contar_bloques),
        "8": ("Contar dígito", r.probar_contar_digito),
        "0": ("Salir", None),
    }

    while True:
        print("TP RECURSIVIDAD")
        for clave, (nombre, _) in opciones.items():
            print(f"{clave}) {nombre}")

        eleccion = input("Elegí un ejercicio para probar: ").strip()

        if eleccion == "0":
            print("¡Listo! Fin del programa.")
            break
        elif eleccion in opciones:
            opciones[eleccion][1]()
        else:
            print("Opción inválida, intentá de nuevo.\n")


if __name__ == "__main__":
    main()