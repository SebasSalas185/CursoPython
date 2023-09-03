Phrase = "El hombre es el único que bebe sin tener sed"

#Metodo starstwith, para validar si una cadena cumple con una posicion indicada 
#Este metodo se usa con cadenas que inicien una cadena (usa enteros positivos como posiciones)
Principio = Phrase.startswith("hombre", 3, 9)
print(Principio)

#Metodo endswith, para validar si una cadena cumple con una posicion indicada 
#Este metodo se usa con cadenas que acaben una cadena (usa enteros negativos como posiciones)
Conclusion = Phrase.endswith("sed", -4, )
print(Conclusion)