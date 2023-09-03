#Funcion range, funciona para determinar un rango de una secuencia numerica
#Posee 3 argumentos, el primero start, el segundo stop y el tercero step

range(100)#Con solo un argumento se formara el stop
#Stop marca el numero en el que se detendra la secuencia, el numero que almacena stop no estara en la secuencia

range(1, 100)#Con dos argumentos se formaran el start y el stop
#Start marca desde que numero se inicia la secuencia

range(1, 100, 10)#Con tres argumentos se formaran el start, el stop y el step
#Step marca el incremento o decremento de la secuencia


#Comportamiento de Range en un bucle for

#Ejemplo de incremento (del 0 al 100 sumando de 10 en 10)
for secuencia in range(0,101,10):
    print(secuencia)

print("\n")

#Ejemplo de decremento (del 100 al 0 restando de 10 en 10)
for secuencia in range(100,0, -10):
    print(secuencia)