animales = []
cantidad = int(input("Ingrese la cantidad de animales: "))
while cantidad!=0:
    animal = input("Ingrese animal: ").strip().capitalize()
    animales.append(animal)
    cantidad-=1

print("lista de animales:\n",animales)