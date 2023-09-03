#La funcion break detiene un bucle while cuando su resultado se cumple
print("While con la sentencia Break \n")
contador = 0

#Bucle hasta que contador sea mayor que 10
while contador < 10:
#Proceso que le suma 1 a contador y determina si es 5, este proceso se repita hasta que contador = 5
	contador += 1 
	if contador == 5:
		#Al cumplirse la condicion la funcion break para el bucle
		break	

	print("Valor actual de la variable: ", contador)
		
print("Fin del proceso.")


#La funcion continue reanuda el bucle while cuando su resultado se cumple
print("\nWhile con la sentencia Continue \n")
contador = 0

#Bucle hasta que contador sea mayor que 10
while contador < 10:
#Proceso que le suma 1 a contador y determina si es 5, este proceso se repita hasta que contador = 5
	contador += 1 
	if contador == 5:
		#Al cumplirse la condicion la funcion continue reanuda el bucle
		continue

	print("Valor actual de la variable: ", contador)

print("Fin del proceso.")