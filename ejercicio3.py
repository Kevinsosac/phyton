print('tarifa por hora')
valor = int(input())
print('horas del dia')
h = int(input())

if h>40:
    sal = valor * h
    bon=sal * 0.2
    print('El valor a pagar es: ', sal+bon)
else:
    sal = valor * h
    print('el valor a pagar es: ', sal) 