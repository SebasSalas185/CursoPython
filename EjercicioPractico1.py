"""Este es un ejercicio practico de un sistema que determina por medio de una clave 
a cual departamento de la empresa forma parte un trabajador, posteriormente, dependiendo
de los años de servicio que lleve trabajando con la empresa se dictamina su periodo de 
vacaciones por medio de un sistema que pide la vigencia del laburo """

print("Bienvenido a la calculadora de periodo de vacaciones \n")

passu = int(input("Digite su clave: "))
pass1 = 3132
pass2 = 4142
pass3 = 6913

if passu == pass1 :
	print("Bienvenido empleado perteneciente al departamento de servicio al cliente\n")
	nom = input("Cual es su nombre?: ")
	res = int(input("\n" + nom + ", introduzca la cantidad de años que lleva trabajando en esta empresa: "))
	if res == 1 :
		print("\n" + nom + ", usted tiene derecho a recibir 6 dias de vacaciones")
	elif res < 7:
		print("\n" + nom + ", usted tiene derecho a recibir 14 dias de vacaciones")
	elif res >= 7 :
	 	print("\n" + nom + ", usted tiene derecho a recibir 20 dias de vacaciones")
	else:
		print("\n" + nom + ", usted aun no tiene derecho a recibir vacaciones")

elif passu == pass2:
	print("Bienvenido empleado perteneciente al departamento de logistica\n")
	nom = input("Cual es su nombre?: ")
	res = int(input("\n" + nom + ", introduzca la cantidad de años que lleva trabajando en esta empresa: " ))
	if res == 1:
		print("\n" + nom + ", usted derecho a recibir 7 dias de vacaciones")
	elif res < 7:
		print("\n" + nom + ", usted tiene derecho a recibir 15 dias de vacaciones")
	elif res < 7:
	 	print("\n" + nom + ", usted tiene derecho a recibir 22 dias de vacaciones")
	else:
		print("\n" + nom + ", usted aun no tiene derecho a recibir vacaciones")

elif passu == pass3:
	print("Bienvenido empleado perteneciente al departamento de Gerencia\n")
	nom = input("Cual es su nombre?: ")
	res = int(input("\n" + nom + ", introduzca la cantidad de años que lleva trabajando en esta empresa: "))
	if res == 1:
		print("\n" + nom + ", usted tiene derecho a recibir 10 dias de vacaciones")
	elif res < 7:
		print("\n" + nom + ", usted tiene derecho a recibir 20 dias de vacaciones")
	if res >= 7:
	 	print("\n" + nom + ", usted tiene derecho a recibir 30 dias de vacaciones")
	else:
		print("\n" + nom + ", usted aun no tiene derecho a recibir vacaciones")

else: 
	print("La clave que ingreso no coincide con ningun departamento")