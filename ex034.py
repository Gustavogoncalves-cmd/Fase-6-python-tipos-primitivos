salario = float(input('qual o salaraio do funcionario? '))
aumento = (salario * (15 / 100)) + (salario)
acima = (salario * (10 / 100)) + (salario)

if salario >= 1250:
    print(f'seu salario + 10% agora e: R${acima:.2f}')
else:
    print(f'seu salario + 15% agora e: R${aumento:.2f}')