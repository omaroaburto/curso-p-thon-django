#ruta ejemplo de ruta
ruta = "C:/python/08-archivos/gente.txt"
archivo = open(ruta, "r")
print(archivo.encoding)
print(archivo.mode)
print(archivo.name) 
#lectura de archivos
print("\nLectura de archivo\nreadline")
print(archivo.readline())
print("\nLectura de archivo\nreadlines")
print(archivo.readlines())
print("\nLectura de archivo\nread")
print(archivo.read())




archivo.close()