from datetime import date
from time import sleep

print('\033[33;1m=' * 10)
print(f'{"ex054":^10}')
print('=' * 10, '\033[m')
sleep(1)

print('\033[1mLeitor da maior idade.')
ano_atual = date.today().year
maiorIdade = 0
menorIdade = 0

for c in range(0, 7):
    anoNas = int(input(f'Quando o {c + 1}°o nasceu? '))
    if ano_atual - anoNas >= 21:
        maiorIdade += 1
    else:
        menorIdade += 1

print(f'''Maiores de idade: {maiorIdade}
Menor de Idade: {menorIdade}\033[m''')