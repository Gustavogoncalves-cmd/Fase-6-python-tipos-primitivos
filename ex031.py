distancia = float(input('qual a distancia da sua viagem? '))
preco = (distancia * 0.50)
promocao = (distancia * 0.45)
if distancia <= 200:
    print(f'sua viagem vai custar R${preco:.2f}')
else:
    print(f'sua viagem teve um desconto e vai custar R${promocao:.2f}')