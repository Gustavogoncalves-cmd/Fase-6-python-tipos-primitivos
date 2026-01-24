nome =str(input('Digite seu nome: '))

if nome == 'Gustavo':
    print('que nome lindo vc tem!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('seu nome e bem popular no Brasil!')
elif nome in 'Ana Claudia Jessica Juliana':
    print('belo nome feminino!')
else:
    print('seu nome e tao normal!')
print(f'bom dia, {nome}!')