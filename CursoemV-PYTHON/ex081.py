from random import randint

contCor = randint(0, 1)
cor = ('\033[1;36m', '\033[1;33m')

print(f'{cor[contCor]}{"81":=^40}\033[m')
ListaDeNum = []
verbo = 'um'

while True:
    add = str(input(f'Digite {verbo} número: '))
    if add.isnumeric():
        valor = int(add)
        ListaDeNum.append(valor)
        
        while True:
            chevron = str(input('Deseja continuar? [S/N] ')).strip().upper()
            if chevron in 'SN':
                break
        if chevron == 'N':
            break
        verbo = 'outro'
    else:
        print('Dígito inválido. Tente novamente.', end=' ')

# Ordenando de forma decrescente manualmente ou usando sort
ListaDeNum.sort(reverse=True)

print(f'\nVocê digitou {len(ListaDeNum)} elementos.')
print(f'Os valores em ordem decrescente são {ListaDeNum}.')
print('O valor 5 ', end='')
if 5 in ListaDeNum:
    print('faz parte da lista!')
else:
    print('não faz parte da lista!')