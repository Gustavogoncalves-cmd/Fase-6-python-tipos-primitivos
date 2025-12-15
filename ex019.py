import random

a1 = str(input('qual o Primeiro aluno: '))
a2 = str(input('qual o Segundo aluno: '))
a3 = str(input('qual o terceiro aluno: '))
a4 = str(input('qual o quarto aluno: '))

lista = [a1, a2, a3, a4]
escolhido = random.choice(lista)
print(f'o aluno escolhido foi {escolhido}')