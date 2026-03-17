from random import randint

contCor = randint(0, 1)
cor = ('\033[1;36m', '\033[1;33m')

print(f'{cor[contCor]}{"78":=^40}\033[m')
valores = []

for c in range(0, 5):
    while True:
        entrada = str(input(f'Digite o {c + 1}º valor: '))
        if entrada.isnumeric():
            valores.append(int(entrada))
            break
        else:
            print('ERRO! Tente novamente!', end=' ')

print(f'Os valores digitados foram {valores}.')

maior = max(valores)
menor = min(valores)

print(f'O maior valor {maior} está nas posições', end=' ')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}... ', end='')

print(f'\nO menor valor {menor} está nas posições', end=' ')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}... ', end='')
print()