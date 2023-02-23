print("Programa para determinar el numero mas grande introducido por el usuario \n")

num1 = int(input("Introduce el primer numero: "))
num2 = int(input("Introduce el segundo numero: "))
num3 = int(input("Introduce el tercer numero: "))

if num1 > num2 and num1 > num3:
	print("\nEl numero", num1, "es el numero mas grande de los tres") 
elif num2 > num1 and num2 > num3:
	print("\nEl numero", num2, "es el numero mas grande de los tres") 
elif num3 > num1 and num3 > num2:
	print("\nEl numero", num3, "es el numero mas grande de los tres") 	