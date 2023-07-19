nombre = input("Digite su nombre por favor: ")
altura = float(input("digite su altura por favor (ejemplo: 1.55): "))
estatura = altura
peso = float(input("Digite su peso en kilogramos"))

imc = peso/estatura**2

if imc >= 0 and imc <= 15.99:
    print(nombre, "estas extremadamente delgado", imc)
elif imc >= 16.00 and imc <= 18.49:
    print(nombre, "estas delgado", imc)
elif imc >= 18.50 and imc <= 24.99:
    print(nombre, "estas en el peso adecuado", imc)
elif imc >= 25.00 and imc <= 29.99:
    print(nombre, "estas en sobrepeso", imc)
elif imc >= 30.00 and imc <= 34.99:
    print(nombre, "estas en obesidad", imc)