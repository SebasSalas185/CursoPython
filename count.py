##El metodo count solo tiene en cuenta los caracteres en su argumento para hacer busquedas
#Estos argumentos las dos coordenadas que representan su posicion en la cadenas

element = "pluton ya no es un planeta"
elmnum = 0

elmnum = element.count("a", 3)
print(f"La frase {element} tiene en total {elmnum} letras A desde la posicion 3")

elmnum = element.count("a", -3)
print(f"La frase {element} tiene en total {elmnum} letras A desde la posicion -3")

elmnum = element.count("a", 0, 22)
print(f"La frase {element} tiene en total {elmnum} letras A desde la posicion 0 hasta la 20")