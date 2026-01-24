n1 = int(input('digite um numero: '))
n2 = int(input('digite outro numero: '))

if n1 >= n2:
    print(f'o primeiro valor {n1} e maior!')
elif n2 >= n1:
    print(f'segundo valor {n2} e maior!')
else:
    print('os dois valores sao iguais!')
