real = float(input('quanto dinheiro vc tem na carteira? '))
dolar = real /5.36
euro = real /6.22
btc = real /468804.62

print(f'com R${real:.2f} vc pode comprar US${dolar:.2f} \n e em €{euro:.2f} ou em BTC {btc:.6f}')