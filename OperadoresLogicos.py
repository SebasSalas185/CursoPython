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
num1 = int(input("Escribe un número mayor a 2 y menor a 5:"))

#Comando if que ejecuta dos condiciones logicas con el operador and
if num1 > 2 and num1 < 5:
    print("El número ", num1, " cumple con la condición.\n")
else:
    print("El número ", num1, " No cumple con la condición.\n")


#Disyunción

#Funcion print para imprimir texto en pantalla
print("Disyunción (or)")

#Variables que almacenan entrada de numeros enteros del usuario
palabra = input("Para cumplir con la condición escribe 'si' o 'yes':")

#Comando if que decide entre dos condiciones logicas con el operador or
if palabra == "si" or palabra == "yes":
    print("La condición se ha cumplido.\n")
else:
    print("La condición NO se ha cumplido.\n")


#Negación

#Funcion print para imprimir texto en pantalla
print("Negación (not)")

#Variables que almacenan entrada de numeros enteros del usuario
num_uno = int(input("Introduce un número igual a 5: "))

#Comando if que niega su condicion logica con el operador not
if not num_uno == 5:
    print("\n El número es diferente de cinco y SI cumple la condición.\n")
else:
    print("\n El número es igual a cinco y NO cumple la condición.\n")