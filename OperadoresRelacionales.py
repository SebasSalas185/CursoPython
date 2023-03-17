"""
Tipos de operadores condicionales:
<	Menor que
>	Mayor que
==	Igual que
!=	No igual a
<=	Menor o igual
>=	Mayor o igual
"""
#Funcion print para imprimir texto en pantalla
print("Introduce dos numeros a comparar \n")

#Variables que almacenan entrada de numeros enteros del usuario
num1 = int(input("Introduce el primer numero: "))
num2 = int(input("Introduce el primer numero: "))

#Funcion print para imprimir texto y variables en pantalla 
print("\nLos numeros a comparar son el", num1, "y el", num2, "\n")

#Comando if por si num1 es igual que num2
if num1 == num2:
	print(num1, "Es igual a", num2)
#Comando if por si num1 es menor que num2	
if num1 < num2:
	print(num1, "Es menor que", num2)
#Comando if por si num1 es mayor que num2
if num1 > num2:
	print(num1, "Es mayor que", num2)
#Comando if por si num1 no es igual que num2
if num1 != num2:
	print(num1, "No es igual a", num2)
#Comando if por si num1 es menor o igual que num2
if num1 <= num2:
	print(num1, "Es menor o igual que", num2)
#Comando if por si num1 es mayor o igual que num2
if num1 >= num2:
	print(num1, "Es mayor o igual que", num2)