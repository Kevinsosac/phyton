nombre = input("digite nombre de el empleado: ")
nuhoras= int(input('digite el numero de horas de trabajo: '))
cuota = float(input('Digite el valor por hora'))

valor = nuhoras * cuota

if nuhoras >=40:
    valorto= valor + (valor * 0.05)
    print(nombre, 'resive de sueldo ', valorto, 'pesos' )
else:
    print(nombre, 'resive de suleldo ', valor)