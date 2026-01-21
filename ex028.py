import random

pergunta = int(input('adivinhe o numero de 1 a 5 que estou pesando! \ndigite aqui o numero: '))

lista = [1, 2, 3, 4, 5]
escolhido = random.choice(lista)

if pergunta == escolhido:
    print('vc acertou, parabens!')
else:
    print('vc errou, o computador venceu!')

print(f'o numero e {escolhido}')