print('Calculadora 3.0')


# Datos de entrada
result = 0
v1 = 0
v2 = 0
salida = False
while salida == False:
     v1 = int(input('Ingrese el primer valor: '))
     v2 = int(input('Ingrese el segundo valor: '))
     operacion = int(input("""Ingrese la operación que quiera realizar: 
                      [0] Salir 
                      [1] Sumar 
                      [2] Restar 
                      [3] Multiplicar 
                      [4] Dividir
                      """))
     # Procesamiento de datos
     if operacion == 1:
          result = v1 + v2
     elif operacion == 2:
          result = v1 - v2
     elif operacion == 3:
          result = v1 * v2
     elif operacion == 4:
          result = v1 / v2
     elif operacion == 0:
          salida = True
          pass
     else:
          print('Operación no válida')
          
     # Salida de información
     print(f'El resultado de la operación es: {result}')
     









