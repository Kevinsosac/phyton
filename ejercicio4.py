nota = float(input('el resultado de la nota es: \n'))

if nota >= 4.5 and nota <= 5.0:
    print('sobresaliente', str(nota))
elif nota >= 4.2 and nota <= 4.4:
    print('notable', str(nota))
elif nota >= 3.8 and nota <= 4.1:
    print('bien', str(nota))
elif nota >= 3.0 and nota <= 3.7:
    print('suficiente', str(nota))
elif nota >= 0.0 and nota <= 2.9:
    print('insuficiente', str(nota))

else: 
    print('Eror: puntuacion invalida', str(nota))