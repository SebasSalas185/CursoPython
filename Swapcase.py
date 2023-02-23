#Metodo .swapcase() (Cambia el formato usado en un simbolo y lo cambia por su formato alterno)
frase = "COMIDA CHATARRA"
print(frase)
print(f"Si cambiamos el formato de mayusculas a minusculas de {frase} quedaria asi: {frase.swapcase()}")

frase1 = "comida chatarra"
print(frase1)
print(f"Si cambiamos el formato de minusculas a mayusculas de {frase1} quedaria asi: {frase1.swapcase()}")

frase2 = "1234!-*"
print(f"Estos otros formatos no son dispuestos a cambios: {frase2.swapcase()}")