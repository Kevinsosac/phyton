galones = int(input('digite la cantidad de galones que desea comprar: '))
litros = float(input('Digite el precio por litro: '))

paga = (galones * 3.78)/1
valortotal = paga * litros

print ('El valor total a pagar es :', valortotal, 'por ', galones, 'galones' )