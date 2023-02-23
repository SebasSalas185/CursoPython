print("Programa que determina numeros pares o impares \n")

num = int(input("Digite un numero: "))
my_num = num / 2

#Se usa la funcion insistance() 
#Devuelve un booleano dependiendo del objeto especificado es del tipo especificado
if isinstance(my_num, int):
    print("El numero", num, "es par")

if isinstance(my_num, float):
    print("El numero", num, "es impar")

else:
	print("El numero no existe")