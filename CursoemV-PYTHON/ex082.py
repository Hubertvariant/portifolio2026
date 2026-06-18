from random import randint

contCor = randint(0, 1)
cor = ('\033[1;36m', '\033[1;33m')

print(f'{cor[contCor]}{"82":=^40}\033[m')
listaCompleta = []
impares = []
pares = []

while True:
    add = ''
    while not add.isnumeric():
        add = str(input('Digite um valor: '))
    
    valor = int(add)
    listaCompleta.append(valor)
    
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)
        
    while True:
        continua = str(input('Deseja continuar? [S/N] ')).strip().upper()
        if continua in 'SN':
            break
    if continua == 'N':
        break

print(f'\nA lista completa: {listaCompleta}')
print(f'Números pares: {pares}')
print(f'Números ímpares: {impares}')