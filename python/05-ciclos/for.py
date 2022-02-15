
for x in range(1,10):
    print(x)


mascotas = {
    "Choco":[5, "perro","m"],
    "Gordito":[3, "gato","m"],
    "Catalina":[10, "gato", "f"],
    "Flecha":[1, "gato","f"],
}

for key in mascotas.keys():
    print("Nombre: {}\n\tedad: {} \n\traza: {} \n\tsexo: {}".format(key, mascotas[key][0],mascotas[key][1],mascotas[key][2]))
