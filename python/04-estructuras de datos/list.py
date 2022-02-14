lista_nombres = ["Pedro", "Alfredo", "Laura", "María"]

while True:
    print("Hola mi nombre es roboto")
    nombre = input("Ingrese su nombre: ").strip().capitalize()
    
    if nombre in lista_nombres:
        print("Bienvenido {}".format(nombre))
        consulta = input("¿Desea eliminar el nombre? (Y/N)\n").strip().lower()
        if consulta == 'y':
            lista_nombres.remove(nombre)
    else:
        print("El nombre {} no está registrado".format(nombre))    
        consulta = input("¿Desea agregar el nombre? (Y/N)\n").strip().lower()
        if consulta == 'y':
            lista_nombres.append(nombre)
    
    consulta = input("¿Desea Salir? (Y/N)\n").strip().lower()
    if consulta == 'y':
        break