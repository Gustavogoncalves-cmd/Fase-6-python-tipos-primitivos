import math
angulo = float(input('digite o angulo que vc deseja: '))
seno = math.sin(math.radians(angulo))
cosceno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))


print(f'o angulo de {angulo} tem o SENO de {seno:.2f}')
print(f'o angulo de {angulo} tem o COSCENO de {cosceno:.2f}')
print(f'tangente de {angulo} tem a TAGENTE de {tangente:.2f}')