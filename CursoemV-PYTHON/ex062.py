from time import sleep

print(f'\033[1;34m{'=' * 10}\n{'ex062':^10}\n{'=' * 10}\033[m')
sleep(1)

p1 = int(input('Digite o primeiro termo: '))
raz = int(input('Digite a razão: '))
if raz == 0:
    raz = 1

termo = p1
cont = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} -> ', end='')
        termo += raz
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados.')