brochas = int(input("digite cuantas brochas desea comprar"))
prebro = int(input("digite el precio unitario de las brochas "))
rodillos = int(input("digite cuantos rodillos desea comprar"))
prero = int(input("digite el precio unitario de los rodillos "))
sellador = int(input("digite cuantos selladores desea comprar"))
prese = int(input("digite el precio unitario de los selladores "))

desbrochas = (prebro - (prebro * 0.2))* brochas
desrodillos = (prero - (prero * 0.15))* rodillos
totalselladores = sellador * prese

valor = desbrochas + desrodillos + totalselladores 

print('1 => de contado')
print('2 =>tarjetas')
respuesta = input('elige una opcion de pago')

if respuesta == '1':
    pagar = valor - (valor * 0.07)
    print('el valor total a pagar es de ', pagar)
else:
    print('El valor total a pagr es de ', valor)