class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def aumentar_edad(self):
        self.age+=1


class Perro(Animal):
    cant_vac = 0
    def __init__(self,name, age, raza, cant_vac):
        super().__init__(name, age)
        self.raza = raza
        self.cant_vac = cant_vac

    def vacunar(self):
        self.cant_vac += 1
    
 

choco = Perro("choco", 5, "perro chico", 2)
print(choco.name)