preço = float(input('qual o preço do produto? R$ '))
novo = preço - (preço * 5 /100)

print(f'o produto que custava {preço:.2f}, na promoção com desconto de 5% vai custar {novo:.2f}')