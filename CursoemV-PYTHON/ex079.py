from random import randint

contCor = randint(0, 1)
cor = ('\033[1;36m', '\033[1;33m')

print(f'{cor[contCor]}{"79":=^40}\033[m')
num = []
verbo = 'um'

while True:
    while True:
        add = str(input(f'Digite {verbo} número: '))
        if add.isnumeric():
            valor = int(add)
            if valor in num:
                print('Valor duplicado! Não vou adicionar...', end=' ')
                verbo = 'outro'
            else:
                print('Adicionado com sucesso...')
                num.append(valor)
                break
        else:
            print('ERRO! Caractere inválido. ', end='')
    
    while True:
        chevron = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if chevron in 'SN':
            break
    
    if chevron == 'N':
        print('Obrigado por utilizar o nosso programa!')
        break
    verbo = 'outro'

print(f'A lista com números únicos em ordem crescente: {sorted(num)}')