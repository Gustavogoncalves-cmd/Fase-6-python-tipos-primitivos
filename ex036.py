valor = float (input('qual o valor da casa? R$'))
salario = float (input('qual o seu salario? R$'))
anos = int(input('em quantos anos voce vai pagar? '))
pestacao = valor / (anos * 12)
minimo = salario * 30 / 100
print(f'para pagar uma casa de R${valor:.2f} em {anos} anos a prestacao sera de R${pestacao:.2f}')
if pestacao <= minimo:
    print('emprestimo pode ser CONCEDIDO!')
else:
    print('emprestimo NEGADO!')