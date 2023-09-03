""" 
Asi se hace una condicional multiple con el comando elif en Python

Declaracion de variables usadas
num1 = 5

Comando if parametrado con la variable num1 en caso de que sea igual a 1
if num1 == 1 :
	print("El numero es Uno")

Comando elif que sirve para otro caso, en este se instruye que sea igual a 2
elif num1 == 2:
	print("El numero es Dos")

Comando else por si no cumple con los requisitos de ningun caso documentado
else :
	print("El numero se desconoce")

print("Fin")
"""

#Funcion print para imprimir texto
print("===============================")
print("Convertidor de numeros a letras")
print("===============================")

#Variable usada para entrada de datos numericos (gracias al comando int())
num = int(input("Cual es el numero que deseas convertir: "))

#Comando if por si variable num es igual a 5
if num == 5 :
	print("El numero es: 'CINCO' ")

#Comando elif por si variable num es igual a 4
elif num == 4 :
	print("El numero es: 'CUATRO' ")

#Comando elif por si variable num es igual a 3
elif num == 3 :
	print("El numero es: 'TRES' ")

#Comando elif por si variable num es igual a 2
elif num == 2 :
	print("El numero es: 'DOS' ")

#Comando elif por si variable num es igual a 1
elif num == 1 :
	print("El numero es: 'UNO' ")	

#Comando else por si no cumple con los requisitos de ningun caso documentado
else: 
	print("No podemos convertir este numero a letras, solo del 1 al 5")

print("Fin")
