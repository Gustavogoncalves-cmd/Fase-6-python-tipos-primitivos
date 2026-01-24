from datetime import date
ano = int(input('em que ano voce nasceu? '))
idade = date.today().year - ano
if idade <18:
    print(f'voce tem {idade} ainda nao vai precisar se alistar ao servico militar!')
    print(f'ainda faltam {18 - idade} anos para o alistamento')
elif idade >=18:
    print(f'voce tem {idade} ja passou do tempo de se alistar ao servico militar!')
    print(f'voce deveria ter se alistado ha {idade - 18} ano')
else:
    print(f'voce tem {idade} anos ja esta na hora de se alistar ao servico militar!')