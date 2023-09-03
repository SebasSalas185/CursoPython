#Metodos para comprobar y convertir palabras de un texto en minusculas o mayusculas en su totalidad 
frase = input("Cual es tu nombre: ")

#Metodo .islower (para comprobar si tiene formato minuscula)
if frase.islower() == False:
	#Metodo .lower (para convertir texto en formato minusculas)
	print("Hola, " +frase+ "\n")
	print(f"Tu nombre con todo en minusculas seria, {frase.lower()} \n")
else:
	print("Tu nombre ya contiene todo en minusculas " +frase.lower()+ "\n" )

#Metodo .isupper (para comprobar si tiene formato mayuscula)
if frase.isupper() == False:
	#Metodo .supper (para convertir texto en formato mayusculas)
	print(f"Tu nombre con todo en mayusculas seria, {frase.upper()} \n")
else:
	print("Tu nombre ya contiene todo en mayusculas " +frase.upper())