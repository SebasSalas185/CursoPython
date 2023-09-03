#El formato correcto de las palabras en Python seria su primera  letra en mayuscula, y el resto en minusculas.

frase = input("Cual es tu nombre: ")

#Metodo .istile (para comprobar si tiene formato correcto)
if frase.istitle() == False:
	#Metodo .istile (para convertir texto en un formato correcto)
	print("Tu nombre esta mal escrito, " +frase.title()+ " seria mas correcto")
	print("Como estas")
else:
	print("Tu nombre esta bien escrito")
	print("Como estas")