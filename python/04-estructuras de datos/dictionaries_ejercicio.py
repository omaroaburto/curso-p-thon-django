movies = {
    "Spiderman": [13,5],
    "Batman": [13,5],
    "Muertos vivientes": [18,5]
} 

while True:
    movie = input("Ingrese la película que desea ver: ").capitalize()
    if(movie in movies):
        age = int(input("Ingrese su edad: "))
        if(age < movies[movie][0]):
            print("La película está retringida para personas mayores de {}".format(movies[movie][0]))
        else:
            entradas = int(input("Ingrese la cantidad de entradas a comprar: "))
            if(entradas <= movies[movie][1]):
                print("Usted ha comprado {} entrads".format(entradas))
                movies[movie][1]-=entradas
            else:
                print("No puede comprar esa cantidad de entradas, quedan {} entradas".format(movies[movie][1]))
            
    else:
        print("Lamentablemente no existe la película o no esta en nuestra cartelera")