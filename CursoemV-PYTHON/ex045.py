from random import randint
from time import sleep

cores = {0: '\033[m', 1: '\033[31;1m'}

print(f'{cores[1]}=' * 10)
print(f'{"ex045":^10}')
print('=' * 10, f'{cores[0]}')
sleep(1)
print('JOKENPÔ')
sleep(1)
print(f'{"[PEDRA]":^9}\n{"[PAPEL]":^9}\n[TESOURA]')
sleep(1)

player = str(input('Qual será a sua jogada? ')).strip().lower()
sleep(1)
print('\033[1;33mJO\033[m ')
sleep(1)
print('\033[1;33mKE\033[m ')
sleep(1)
print('\033[1;33mPÔ\033[m ')

computador = randint(0, 2)
item = ['Pedra', 'Papel', 'Tesoura']
print(item[computador], end=' ')

if computador == 0: # pedra
    if player == 'pedra':
        print('\033[33;1mEMPATE!\033[m')
    elif player == 'papel':
        print('\033[32;1mVITÓRIA!\033[m')
    elif player == 'tesoura':
        print('\033[31;1mDERROTA!\033[m')
    else:
        print('INVALIDO')
elif computador == 1: # papel
    if player == 'papel':
        print('\033[33;1mEMPATE!\033[m')
    elif player == 'tesoura':
        print('\033[32;1mVITÓRIA!\033[m')
    elif player == 'pedra':
        print('\033[31;1mDERROTA!\033[m')
    else:
        print('INVALIDO')
else: # tesoura
    if player == 'tesoura':
        print('\033[33;1mEMPATE!\033[m')
    elif player == 'pedra':
        print('\033[32;1mVITÓRIA!\033[m')
    elif player == 'papel':
        print('\033[31;1mDERROTA!\033[m')
    else:
        print('INVALIDO')