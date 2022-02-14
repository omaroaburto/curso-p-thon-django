frase = "El camino para llegar al éxito es muy largo, pero si te esfuerzas serás recompenzado. Es el principio que rige el mundo, dentro de este universo."

#contar palabraras
my_string = "El" 
contar = frase.count(my_string)
print("La palabra ", contar)

texto = "hola Mundo"
print(texto)
print("La siguiente frase utiliza minúsculas: ",texto.lower())
print("La siguiente frase utiliza mayúsculas: ", texto.upper())
print("La siguiente frase está capitalizada: ", texto.capitalize())
print("La primera palabra de la siguiente frase utiliza mayúsculas : ", texto.title())

#métodos para consultar si se cumple una condición del stream
# texto.islower() consulta si todos los caracteres son minúsculas
# texto.isupper() consulta si todos los caracteres son utiliza mayúsculas
# texto.isalpha() consulta si todos los caracteres son alfabéticos
# texto.isdigit() consulta si todos los caracteres son dígitos
# texto.isalnum() consulta si todos los caracteres son alfanuméricos
#regresa la posición donde se encuentra una palabra
print(texto.index("Mundo")) #en caso de no encontrar el texto arroja un error
#print(texto.index("asdfafo")) error
#es similar a index, pero en caso de no encontrar algo retorna un -1
print(texto.find("hola"))
#print(texto.find("Holssa")) retorna -1


print(texto[:2])