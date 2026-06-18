from time import sleep

print(f'\033[1;34m{'=' * 10}\n{'ex061':^10}\n{'=' * 10}\033[m')
sleep(1)

print('termos com while')
p1 = int(input('Digite o primeiro termo: '))
raz = int(input('Digite a razão: '))
termo = p1
cont = 1

while cont <= 10:
    print(termo, end=' -> ')
    termo += raz
    cont += 1
print('FIM!')