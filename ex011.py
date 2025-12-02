largura = float(input('largura da parede: '))
alt = float(input('altura da parede: '))
área = largura * alt
tinta = área / 2

print(f'sua parede tem a dimensão de {largura}x{alt} e sua área é de {área}m²')
print(f'para Pintar essa parede, vc de {tinta}L de tinta')