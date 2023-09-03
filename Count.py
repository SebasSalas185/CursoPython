##El metodo count solo tiene en cuenta los caracteres en su argumento para hacer busquedas
#Estos argumentos las dos coordenadas que representan su posicion en la cadenas

element = "pluton ya no es un planeta"
elmnum = 0

#En el metodo, lo que se ponga como string sera lo que se buscara en la cadena
elmnum = element.count("a")
print(f"\nLa frase {element} tiene en total {elmnum} letras A \n")

#En el metodo, el numero que se ponga de segundo argumento sera la posicion inicial
elmnum = element.count("a", -3)
print(f"La frase {element} tiene en total {elmnum} letras A desde la posicion -3\n")

#En el metodo, el numero que se ponga de tercer argumento sera la posicion final
elmnum = element.count("a", 0, 22)
print(f"La frase {element} tiene en total {elmnum} letras A desde la posicion 0 hasta la 20\n")