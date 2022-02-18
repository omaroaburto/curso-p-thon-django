
def funcion_principal(funcion_parametro):
    print("Dentro de la función principal")

    def funcion_ejecutar(nom):
        print("Dentro de función ejecutar")
        return funcion_parametro(nom)
    
    return funcion_ejecutar


def saludo(nombre):
    print("Saludos {}!!".format(nombre))

def pregunta(nombre):
    print("¿Cómo estás {} ?".format(nombre))


respuesta = funcion_principal(saludo)
respuesta("Rosa")