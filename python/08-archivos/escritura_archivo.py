#ruta ejemplo de ruta
ruta = "C:/Users/omaro/OneDrive/Desktop/curso de python/python/08-archivos/mascotas.txt"
with open(ruta, "w") as archivo: #es otra forma para trabajar con archivos
    #a continuación, vamos hacer un ejercicio para ingresar muchas mascotas
    print("Ingrese de mascotas")
    while(True):
        nombre = input("Ingrese el nombre de la mascota: ").capitalize()
        edad= input("ingrese la edad de la mascota: ")
        archivo.write("{}, {}\n".format(nombre, edad))
        continuar = input("Desea continuar, ingrese (N) para finalizar...")
        if(continuar == "N"):
            break;

