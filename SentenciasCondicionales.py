#Funcion print para imprimir texto en pantalla
#Comando \n es para salto de linea
print("=========")
print("Conversor")
print("========= \n")

print("Menu de opciones: \n")

print("Presiona 1 para convertir de numero a palabra \n")
print("Presiona 2 para convertir de palabra a numero \n")

#Variable que almacena la entrada de numeros enteros enteros de un usuario
opc = int(input("Cual es tu opcion deseada?: "))

#Comando if por si opc es igual a 1
if opc == 1:
#Declaracion de Instrucciones

	#Funcion print que imprime texto junto a un salto de linea
	print("Conversor de numero a palabra \n")

	#Variable que almacena la entrada de numeros enteros de un usuario
	num = int(input("Digite un numero: "))

	#Comando if por si la variable num es igual a 5
	if num == 5 :
		print("El numero es: 'cinco' ")

	#Comando elif por si la variable num es igual a 4
	elif num == 4 :
		print("El numero es: 'cuatro' ")

	#Comando elif por si la variable num es igual a 3
	elif num == 3 :
		print("El numero es: 'tres' ")

	#Comando elif por si la variable num es igual a 2
	elif num == 2 :
		print("El numero es: 'dos' ")

	#Comando elif por si la variable num es igual a 1	
	elif num == 1 :
		print("El numero es: 'uno' ")
	
	#Comando else por si no se cumple ninguno de los casos de num
	else: 
		print("No podemos convertir este numero a letras, solo del 1 al 5")

#Comando if por si opc es igual a 2
elif opc == 2 :
#Declaracion de Instrucciones

	#Funcion print que imprime texto junto a un salto de linea
	print("Conversor de numero a palabra. \n")

	#Variable que almacena la entrada de texto de un usuario
	pal = input("Digite un numero hecho palabra: ")
	#Variable pal guarda su texto contenido convertido en minusculas
	#Gracias al comando .lower() se puede modificar todo un texto a minusculas  
	pal = pal.lower()

	#Comando if por si la variable pal es igual a "cinco" 
	if pal == "cinco" :
		print("El numero es: '5' ")

	#Comando elif por si la variable pal es igual a "cuatro"	
	elif pal == "cuatro" :
		print("El numero es: '4' ")

	#Comando elif por si la variable pal es igual a "tres"
	elif pal == "tres" :
		print("El numero es: '3' ")

	#Comando elif por si la variable pal es igual a "dos"	
	elif pal == "dos" :
		print("El numero es: '2' ")

	#Comando elif por si la variable pal es igual a "uno"
	elif pal == "uno" :
		print("El numero es: '1' ")

	#Comando else por si no se cumple ninguno de los casos de pal	
	else: 
		print("No podemos convertir esta palabra a un numero, solo del uno al cinco")

#Comando else por si no se cumple ninguno de los casos de opc
else :
	print("No ha elegido una opcion valida")

print("Fin")