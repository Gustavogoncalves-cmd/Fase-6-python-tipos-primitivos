n1 = float(input('digite a primeira nota: '))
n2 = float(input('digite a segunda nota: '))
m = (n1 + n2)/2

if m > 7.0:
    print('sua media foi otima, parabens!')
    print(f'com {m:.1f} de media, vc foi aprovado!')
elif m == 6.9 or m == 5.0:
    print('sua media foi ruim, vamos melhorar!')
    print(f'com {m:.1f} de media, vc foi para a recuperacao!')
else:
    m < 5.0
    print('sua media foi pessima, estude mais!')
    print(f'com {m:.1f} de media, vc esta reprovado!')