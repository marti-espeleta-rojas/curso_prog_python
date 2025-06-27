from cmath import sqrt

# Cálculo de discriminante
def calculoDiscriminante(a, b, c):
    discriminante = pow(b, 2) - 4 * a * c
    return discriminante


def calculoResolvente(a, b, c):
    discriminante = calculoDiscriminante(a, b, c)
    if (discriminante == 0):
        calculoResolventeIgualA0(a, b, c)
    elif (discriminante > 0):
        calculoResolventeMayorA0(a, b, c)
    else:
        print("Discriminante negativo. No se puede resolver en el dominio de los números reales")

# Calular resolvente para discriminante igual a 0
def calculoResolventeIgualA0(a, b, c):
    discriminante = calculoDiscriminante(a, b, c)
    resultado = ((- b + sqrt(discriminante))/2*a)
    print(f"El resultado de la raíz para los números a: {a}, b: {b}, c: {c} es... ¡{resultado}!")

# Calular resolvente para discriminante igual a 0
def calculoResolventeMayorA0(a, b, c):
    discriminante = calculoDiscriminante(a, b, c)
    resultadoPositivo = ((- b + sqrt(discriminante))/2*a)
    resultadoNegativo = ((- b - sqrt(discriminante))/2*a)
    print(f"El resultado de la raíz para los números a: {a}, b: {b}, c: {c} es... X1 = {resultadoPositivo}; X2 = {resultadoNegativo}")


# Solicitar datos de entrada
a = input(float("Ingrese el parámetro a: "))
b = input(float("Ingrese el parámetro b: "))
c = input(float("Ingrese el parámetro c: "))

calculoResolvente(a, b, c)


