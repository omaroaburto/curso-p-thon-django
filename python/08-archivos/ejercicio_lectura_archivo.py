#ruta ejemplo de ruta
ruta = "C:/python/08-archivos/gente.txt"
archivo = open(ruta, "r")
 

for persona in archivo.readlines():
    aux1 = persona.split(",") 
    print("Nombre: {} - Edad: {}".format(aux1[0], aux1[1].rstrip("\n")))