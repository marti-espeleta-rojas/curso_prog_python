# Función con parámetros y sin retorno

# Declaración y definición de funciones
def operaciones(a, b, c):
    suma = a + b + c
    print(f"La suma de {a} + {b} + {c} es igual a: {suma}")
    resta = a - b - c
    print(f"La resta de {a} + {b} + {c} es igual a: {resta}")
    multiplicacion = a*b*c
    print(f"La multiplicación de {a} + {b} + {c} es igual a: {multiplicacion}")
    division = a / b / c
    print(f"La división de {a} + {b} + {c} es igual a: {suma}")

# Datos de entrada
a = int(input("Ingrese el primer valor: "))
b = int(input("Ingrese el primer valor: "))
c = int(input("Ingrese el primer valor: "))

# Llamada a función 
operaciones(a,b,c)