from random import randint

contCor = randint(0, 1)
cor = ('\033[1;36m', '\033[1;33m')

print(f'{cor[contCor]}{"075":=^40}\033[m')

num = (int(input('Digite o 1º valor: ')),
       int(input('Digite o 2º valor: ')),
       int(input('Digite o 3º valor: ')),
       int(input('Digite o 4º valor: ')))

print(f'O número 9 apareceu {num.count(9)} vezes.')

if 3 in num:
    print(f'O número 3 apareceu na {num.index(3) + 1}ª posição.')
else:
    print('O número 3 não foi digitado.')

print('Os valores pares digitados foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
print()