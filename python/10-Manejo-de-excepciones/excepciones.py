

def dividir(x, y):
    try:
         print(x/y) 
    except ZeroDivisionError:
        print("No se puede dividir por cero") 
    finally:
        print("Fin")


#########
try:
    a = int(input("Ingrese el valor A: "))
    b = int(input("Ingrese el valor B: "))

    dividir(a,b)
except Exception as error:
    #print(type(error))
    print("Lo siento, hubo un error", error)
