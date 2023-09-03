"""
Tipos de operadores logicos:

Conjuncion(and): Sirve para que se ejcute mas de una condicion logica
Disyuncion(or): Sirve para que se ejecute una de dos o mas condiciones logicas
Negacion(not): Sirve como la instruccion de una condicion logica de forma negativa
"""
#Conjución

#Funcion print para imprimir texto en pantalla
print("Conjunción (and)")

#Variables que almacenan entrada de numeros enteros del usuario
num1 = int(input("Escriba un numero del 2 al 5:"))

#Comando if que ejecuta dos condiciones logicas con el operador and
if num1 >= 2 and num1 <= 5:
    print("El número ", num1, " es un numero correcto\n")
else:
    print("El número ", num1, " no cumple con la condición propuesta.\n")


#Disyunción

#Funcion print para imprimir texto en pantalla
print("Disyunción (or)")

#Variables que almacenan entrada de numeros enteros del usuario
palabra = input("Para cumplir con la condición escribe 'si' o 'yes':")

#Comando if que decide entre dos condiciones logicas con el operador or
if palabra == "si" or palabra == "yes":
    print(f"Acaba de escribir {palabra}.\n")
else:
    print("La condición no se ha cumplido.\n")


#Negación

#Funcion print para imprimir texto en pantalla
print("Negación (not)")

#Variables que almacenan entrada de numeros enteros del usuario
num_uno = int(input("Introduce un número diferente a 5: "))

#Comando if que niega su condicion logica con el operador not
if not num_uno == 5:
    print("El número es diferente a 5 y si cumple la condición.\n")
else:
    print("El número es igual a 5 y no cumple la condición.\n")