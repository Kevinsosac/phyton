productos = input("que producto desea llevar: ")
valor = int(input("digite el valor de su articulo: "))

if valor < 30:
    print('su', productos, 'cuesta', valor)
elif valor >=30 and valor <=60:
    valorto= valor + (valor * 0.3)
    print('su', productos, 'cuesta', valorto)
elif valor > 60 and valor < 400:
    valortotal = valor + (valor * 0.4)
    print('su', productos, 'cuesta', valortotal)
elif valor >= 400:
    pagar= valor + (valor * 0.5)
    print('su', productos, 'cuesta', pagar)
