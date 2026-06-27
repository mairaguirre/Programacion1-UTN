# practico_11_recursividad.py
# Práctico 11: Aplicación de la Recursividad


# ============================================================
# 1) Factorial de un número (recursivo)
# ============================================================
def factorial(n):
    # Caso base: el factorial de 0 (y de 1) es 1
    if n <= 1:
        return 1
    # Caso recursivo: n! = n * (n-1)!
    return n * factorial(n - 1)


def mostrar_factoriales():
    num = int(input("Ingrese un número entero: "))
    for i in range(1, num + 1):
        print(f"Factorial de {i} = {factorial(i)}")
    print()


# ============================================================
# 2) Serie de Fibonacci (recursivo)
# ============================================================
def fibonacci(n):
    # Casos base: fib(0) = 0, fib(1) = 1
    if n == 0:
        return 0
    if n == 1:
        return 1
    # Caso recursivo: fib(n) = fib(n-1) + fib(n-2)
    return fibonacci(n - 1) + fibonacci(n - 2)


def mostrar_fibonacci():
    num = int(input("Ingrese hasta qué posición mostrar la serie de Fibonacci: "))
    for i in range(num + 1):
        print(f"Fibonacci({i}) = {fibonacci(i)}")
    print()


# ============================================================
# 3) Potencia: n^m = n * n^(m-1)
# ============================================================
def potencia(base, exponente):
    # Caso base: cualquier número elevado a 0 es 1
    if exponente == 0:
        return 1
    # Caso recursivo: n^m = n * n^(m-1)
    return base * potencia(base, exponente - 1)


def probar_potencia():
    base = float(input("Ingrese la base: "))
    exp = int(input("Ingrese el exponente (entero >= 0): "))
    print(f"{base} ^ {exp} = {potencia(base, exp)}")
    print()


# ============================================================
# 4) Decimal a binario (recursivo)
# ============================================================
def decimal_a_binario(n):
    # Caso base: cuando el número llega a 0, no hay más restos que agregar
    if n == 0:
        return ""
    # Caso recursivo: convierto el cociente (n // 2) y le agrego el resto actual
    return decimal_a_binario(n // 2) + str(n % 2)


def probar_decimal_a_binario():
    try:
        num = int(input("Ingrese un número decimal positivo (entero, sin coma): "))
    except ValueError:
        print("Entrada inválida. Ingresá solo números enteros.\n")
        return

    if num == 0:
        print("Binario: 0\n")  # caso especial: el 0 no entra en la recursión normal
    else:
        print(f"Binario: {decimal_a_binario(num)}\n")


# ============================================================
# 5) Palíndromo (recursivo, sin [::-1] ni reversed())
# ============================================================
def es_palindromo(palabra):
    # Caso base: una palabra de 0 o 1 letras siempre es palíndromo
    if len(palabra) <= 1:
        return True
    # Caso recursivo: si el primer y último carácter coinciden,
    # reviso recursivamente el resto de la palabra (sin los extremos)
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])


def probar_palindromo():
    texto = input("Ingrese una palabra (sin espacios ni tildes): ").lower()
    if es_palindromo(texto):
        print(f"'{texto}' ES un palíndromo.\n")
    else:
        print(f"'{texto}' NO es un palíndromo.\n")


# ============================================================
# 6) Suma de dígitos (recursivo, sin convertir a string)
# ============================================================
def suma_digitos(n):
    # Caso base: si el número tiene un solo dígito, la suma es el número mismo
    if n < 10:
        return n
    # Caso recursivo: último dígito (n % 10) + suma de dígitos del resto (n // 10)
    return n % 10 + suma_digitos(n // 10)


def probar_suma_digitos():
    num = int(input("Ingrese un número entero positivo: "))
    print(f"Suma de dígitos de {num} = {suma_digitos(num)}\n")


# ============================================================
# 7) Contar bloques de la pirámide (recursivo)
# ============================================================
def contar_bloques(n):
    # Caso base: con 1 bloque en el nivel más bajo, solo hay 1 bloque en total
    if n == 1:
        return 1
    # Caso recursivo: los bloques del nivel actual + los de la pirámide de n-1
    return n + contar_bloques(n - 1)


def probar_contar_bloques():
    num = int(input("Ingrese la cantidad de bloques del nivel más bajo: "))
    print(f"Total de bloques necesarios: {contar_bloques(num)}\n")


# ============================================================
# 8) Contar apariciones de un dígito en un número (recursivo)
# ============================================================
def contar_digito(numero, digito):
    # Caso base: si no quedan más dígitos por revisar, no hay más coincidencias
    if numero == 0:
        return 0
    # Comparo el último dígito del número con el dígito buscado
    coincide = 1 if numero % 10 == digito else 0
    # Caso recursivo: sumo la coincidencia actual + lo que aparece en el resto del número
    return coincide + contar_digito(numero // 10, digito)


def probar_contar_digito():
    num = int(input("Ingrese un número entero positivo: "))
    dig = int(input("Ingrese el dígito a contar (0-9): "))
    print(f"El dígito {dig} aparece {contar_digito(num, dig)} veces en {num}\n")


