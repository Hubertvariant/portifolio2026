from random import randint
from time import sleep

c = {0: '\033[m', 1: '\033[36m', 2: '\033[33m', 4: '\033[32m', 5:'\033[31m'}

print(f'{c[1]}=' * 20)
print(f'{c[2]}ex028')
print(f'{c[1]}={c[0]}' * 20)

print(f'Vou pensar em um numero entre 0 e 5,{c[1]} tente adivinhar{c[0]}!!!')
print('pensando...')
sleep(2)
nC = int(randint(0, 5))
nU = int(input('Ok. que número eu pensei? '))
sleep(2)
print(f'Você {c[4]}acertou{c[0]}!!! meu número era {nC}' if nC == nU else f'Você {c[5]}errou{c[0]}! meu número era {nC}')