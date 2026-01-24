from datetime import date

ano = int(input('em que ano voce nasceu? '))
idade = date.today().year - ano

if idade <9:
    print(f'voce tem {idade} anos. sua categoria MIRIM')
elif idade <=14:
    print(f'voce tem {idade} anos. sua categoria e INFANTIL')
elif idade <=19:
    print(f'voce tem {idade} anos. sua categoria e JUNIOR')
elif idade <=20:
    print(f'voce tem {idade} anos. sua categoria e SENIOR')
else:
    print(f'voce tem {idade} anos. sua categoria e MASTER')