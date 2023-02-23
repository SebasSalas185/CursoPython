#Ejemplo del uso de la sentencia Break
#Esta funcion detiene un bucle while cuando su resultado es verdadero, ejecutando sus instrucciones
print("while con la sentencia Break \n")
contador = 0

while contador < 10:
	contador += 1 

	if contador == 5:
		break

	print("Valor actual de la variable: ", contador)

print("Fin del programa.")

#Ejemplo del uso de la sentencia Continue
#Esta funcion continua el bucle while cuando su resultado es verdadero, ejecutando sus instrucciones
print("\nWhile con la sentencia Continue \n")
contador = 0

while contador < 10:
	contador += 1 

	if contador == 5:
		continue

	print("Valor actual de la variable: ", contador)

print("Fin del programa.")