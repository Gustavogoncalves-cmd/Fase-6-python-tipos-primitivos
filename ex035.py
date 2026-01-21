print('-='*20)
print('analisador de triangulos')
print('-='*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('os seguimentos acima PODEM FORMAR triangulo!')
else:
    print('os segmento acima NAO PODEM FORMAR triangulo!')