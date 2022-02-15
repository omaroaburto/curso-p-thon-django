def sumar(x,y):
    return x+y

def saludar(nombre="juanito",edad=10):
    saludo = "Hola, mi nombre es {} y tengo {} años".format(nombre, edad)
    return saludo


def sumar_numeros(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total

print(sumar(2,3))
print(saludar("pedro", 5))
print(saludar())
print(sumar_numeros(2,3,4,5,6))

persona = {
    "nombre":"Pedro",
    "edad":13 
}
print(saludar(**persona))