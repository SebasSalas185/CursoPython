"""
Asi se hace una condicional compu con el comando if else en Python

Declaramos las variables que queremos usar
num1 = 5

Con el comando if colocamos los parametros para la instruccion
En caso de que se cumpla este caso, ejecutara las intrucciones demandadas

if num1 == 5:
	Ejecutamos la(s) instruccion(es) para este caso
	print("El numero es 5")

Con el comando else declaramos intrucciones de ser el caso contrario del if  
else :
	Ejecutamos la(s) instruccion(es) para este caso
	print("El numero no es 5")

"""

#Funcion print para imprimir texto
print("Sistema para calificar promedio")
#Variable usada para entrada de datos del usuario
name = input("Para empezar, cual es tu nombre?: ")

#Variables usadas para entrada de datos numericos (gracias al comando int())
note1 = int(input(name + ", Cual es tu calificacion en matematicas?: "))
note2 = int(input(name + ", Cual es tu calificacion en quimica?: "))
note3 = int(input(name + ", Cual es tu calificacion en biologia?: "))

#Variable que guarda la suma de las anteriores variables
res = note1 + note2 + note3
#Variable prom que guarda la division de res entre 3
prom = res / 3

#Comando If que realiza una comparacion con el numero 7 
#Caso para verificar que prom sea mayor o igual a 7 
if prom >= 7:
	#Instruccion para imprimir en pantalla el resultado del promedio
	#Metodo round para el conteo de decimales
	print("Felicidades " + name + ", aprobaste con un promedio de: ", prom)
	print("Felicidades " + name + ", aprobaste con un promedio de: ", round(prom, 2))

#Comando else por si no se cumple con lo solicitado por el comando if
else:
	#Instruccion para imprimir en pantalla el resultado del promedio
	#Metodo round para el conteo de decimales
	print("Lamentablemente " + name + ", reprobaste con un promedio de: ", prom)
	print("Lamentablemente " + name + ", reprobaste con un promedio de: ", round(prom, 2))

print("Estoy para servirte")