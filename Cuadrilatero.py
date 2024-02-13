valor1 = input("Ingresa un valor: ")
valor2 = input("Ingresa un valor: ")
valor3 = input("Ingresa un valor: ")
valor4 = input("Ingresa un valor: ")

if valor1 == valor2 == valor3 == valor4:
    print("El objeto es un cuadrado")
elif (valor1 == valor2 and valor3 == valor4) or (valor1 == valor3 and valor2 == valor4) or (valor1 == valor4 and valor2 == valor3):
    print("El objeto es un rectángulo")
else:
    print("El objeto es un cuadrilátero")
