nombre = input("digite su nombre")
modelo = input("Digite el modelo el traje: ")
cantidad = int(input('digite la cantidad de trajes que desea comprar '))
precio = int(input('digite el precio unotario del traje '))

valor= cantidad * precio

if cantidad >= 3:
    valortotal= valor - (valor * 0.17)
    print(nombre, 'el precio de tus trajes es de ', valortotal)
else:
    print(nombre, 'el precio de tus trajes es de ', valor)