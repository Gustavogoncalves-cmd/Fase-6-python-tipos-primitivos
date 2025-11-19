n1=int(input('Digite um valor! '))
n2=int(input('outro valor: '))
s= n1+n2
m= n1*n2
d= n1/n2
di= n1//n2
e= n1**n2

print(f'a soma e {s}, o produto e {m}, e a divisao e {d:.3f}', end=' ') #sempre lembrar que ao final do codigo. adicionar uma virgula e depois o end! ex: ( , end='')
print(f'divisao inteira {di}, e potencia {e}')