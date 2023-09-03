#Funcion If, actua como una condicional de una cadena de funcional

#Funcion print para imprimir texto
print("Sistema para calificar promedio")
#Variable para guardar entrada de datos del usuario
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
	
	print("Felicidades " + name + ", aprobaste con un promedio de: ", prom)

#Comando If que realiza una comparacion con el numero 7 
#Caso para verificar que prom sea menor a 7 
if prom < 7:
	
	print("Lamentablemente " + name + ", reprobaste con un promedio de: ", prom)

print("Estoy para servirte")