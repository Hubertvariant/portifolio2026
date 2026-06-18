from random import randint

contCor = randint(0, 1)
cor = ('\033[1;36m', '\033[1;33m')

print(f'{cor[contCor]}{"074":=^40}\033[m')
numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

print('Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')

print(f'\nO maior valor foi {max(numeros)}')
print(f'O menor valor foi {min(numeros)}')