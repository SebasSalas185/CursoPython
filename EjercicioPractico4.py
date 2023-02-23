print("Calculadora \n")

num = int(input("Digite el primer numero de la operacion: "))
sig = input("Digite el operador usado de la operacion: ")

if sig == "+":
	num += int(input("Digite el segundo numero de la operacion: "))
	print("El resultado de la suma es", num)

elif sig == "-":
	num -= int(input("Digite el segundo numero de la operacion: "))
	print("El resultado de la resta es", num)

elif sig == "*":
	num *= int(input("Digite el segundo numero de la operacion: "))
	print("El resultado de la multiplicacion es", num)

elif sig == "/":
	num /= int(input("Digite el segundo numero de la operacion: "))
	print("El resultado de la division es", num)

elif sig == "**":
	num **= int(input("Digite el segundo numero de la operacion: "))
	print("El resultado del exponente es", num)

elif sig == "%":
	num %= int(input("Digite el segundo numero de la operacion: "))
	print("El resultado del modulo es", num)

elif sig == "//":
	num //= int(input("Digite el segundo numero de la operacion: "))
	print("El resultado de la division entera es", num)

else:
	print("Lo sentimos, la operacion con ese operador no esta disponible")