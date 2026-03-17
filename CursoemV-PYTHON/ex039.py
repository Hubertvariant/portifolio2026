from datetime import date
from time import sleep

cores = {0: '\033[m', 1: '\033[31;1m'}

print(f'{cores[1]}=' * 10)
print(f'{"ex039":^10}')
print(f'=' * 10, f'{cores[0]}')
sleep(1)

print('\033[1mSentido!\033[m Soldado!')
atual = date.today().year
nas = int(input('Quando você nasceu soldado? '))
idade = atual - nas
sleep(1)

print(f'Soldado você tem {idade} anos.', end=' ')
if idade < 17:
    print(f'Falta {17 - idade} anos. \033[1;33mAinda vai se alistar\033[m\033[1m ao serviço militar.')
elif idade < 19:
    print('\033[1;33mHora de se alistar.\033[m')
else:
    print(f'{idade - 18} anos. \033[1;33mPassou do tempo\033[m \033[1mdo alistamento.\033[m')
sleep(1)