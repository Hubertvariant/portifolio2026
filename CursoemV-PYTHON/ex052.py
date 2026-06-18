print('\033[33;1m=' * 10)
print(f'{"ex052":^10}')
print('=' * 10, '\033[m')

print('\033[1mIDENTIFICADOR DE NÚMEROS PRIMOS!')
num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[34;1m', end=' ')
        tot += 1
    else:
        print('\033[m', end=' ')
    print(f'{c}', end='')
print('\033[m')
if tot > 2:
    print('\033[1mNão é primo!\033[m')
else:
    print('\033[1mÉ primo!\033[m')