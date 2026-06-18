from time import sleep

print('\033[33;1m=' * 10)
print(f'{"ex048":^10}')
print('=' * 10, '\033[m')
sleep(1)

print('\033[1mSOMA DE NÚMEROS IMPARES, DIVISIVEIS POR 3, NO INTERVALO DE 1 ÁTE 500\033[m')
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        soma += c
print(f'\033[33;1mA SOMA de todos os {cont} números impares, divisiveis por 3 e no intervalo de 1 áte 500: {soma}\033[m')