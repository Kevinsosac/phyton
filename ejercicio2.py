numero1 = int(input('ingrese el primer numero: '))
numero2 = int(input('ingrese el segundo numero: '))

print("Que operacion desea hacer: ")
print("a => suma")
print("b => resta")
print("c => multiplicacion")
print("d => division")

operacion = input("eliga una opcion: ")
if operacion == "a":
    suma = numero1 + numero2
    print("el resultado es: ", suma)
elif operacion == "b":
    resta = numero1 - numero2
    print("el resultado es: ", resta)
elif operacion == "c":
    mul = numero1 * numero2
    print("el resultado es: ", mul)
elif operacion == "d":
    div = numero1 / numero2
    print("el resultado es: ", div)