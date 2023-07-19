largo = float(input('digite el largo del terreno (en metros cuadrdados)'))
ancho = float(input("digite el ancho del terreno (en metros cuadrados)"))
precio = float(input('Digite el precio por metro cuadrado: '))

terreno = largo * ancho
Valor = precio * terreno

if terreno > 400:
    valort = Valor - (Valor * 0.1)
    print('el precio del terreno es de ', valort)
else:
    print('el precio de el terreno es de ', Valor)
