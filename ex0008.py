medida = float(input('uma distancia em metros: '))
km = medida / 1000
hm = medida / 100
dam = medida / 10
cm = medida * 100
mm = medida * 1000

print(f'\n a medida de {medida}m corresponde a\n {km}km \n {hm} \n {dam} \n {cm:.0f}cm \n {mm:.0f}mm')