numero = int(input('digite um numero inteiro: '))
escolha = int(input('''escolha uma das bases para conversao:
[1] converter para BINARIO
[2] COVERTER PARA OCTAL
[3] converter para HEXADECIMAL
'''))

if escolha == 1:
    print(f'o numero {numero} convertido para BINARIO e igual a {bin(numero)[2:]}')
elif escolha == 2:
    print(f'o numero {numero} convertido para OCTAL e igual a {oct(numero)[2:]}')
elif escolha == 3:
    print(f'o numero {numero} convertido para HEXADECIMAL e igual a {hex(numero)[2:]}')