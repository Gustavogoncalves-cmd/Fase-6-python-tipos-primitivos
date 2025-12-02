dias = int(input(' quantos dias vc rodou com o carro? '))
km = float(input('quantos km rodados? '))

diasR = int(60)
kmR = int(0.15)
valor = (dias * 60) + (km * 0.15)


print(f'rodados {dias} dias e {km} kms o valor em debito e de {valor:.2f} ')