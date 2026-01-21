v = float(input('qual era velocidade do carro: '))
if v > 80:
    print(f'MULTADO! Voce excedeu o limite permitido que e de 80km/h')
    multa = (v-80) * 7
    print('vc deve pagar uma multa de R${:.2f}'.format(multa))

print(f'tenha um bom dia! dirija com segurança!')