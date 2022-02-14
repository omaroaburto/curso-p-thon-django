num1 = input("Ingrese el primer número: ")
num2 = input("Ingrese el segundo número: ")

if(num1 < num2):
    print("El primer número es menor que el segundo número")
elif(num1 == num2):
    print("El primer número es igual que el segundo número")
else:
    print("El primer número es mayor que el segundo número")




nombre = input("Ingrese una palabra con menos de 10 letras: ")

if(len(nombre)<10 and nombre.isalpha()):
    print("La palabra es válida")
else:
    print("la palabra es inválida")
