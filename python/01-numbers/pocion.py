import random

salud = 50
dificultad = 1
pocion_salud = int(random.randint(25, 50) / dificultad)
salud = salud + pocion_salud
print(salud)