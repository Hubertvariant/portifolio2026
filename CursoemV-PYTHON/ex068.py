from random import randint
from time import sleep

while True:
    print(f'\033[1;36m{"=" * 10}\n{"ex068":^10}\n{"=" * 10}\033[m')
    vitorias = 0
    
    while True:
        computer = randint(0, 10)
        number = int(input('\033[1mDiga um número: '))
        escolha = ' '
        while escolha not in 'IP':
            escolha = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]

        print('PAR...')
        sleep(0.5)
        print('OU...')
        sleep(0.5)
        print('ÍMPAR!')
        
        total = computer + number
        tipo = 'P' if total % 2 == 0 else 'I'
        
        print(f'Você jogou {number} e o computador {computer}. Total de {total} ', end='')
        print('DEU PAR' if tipo == 'P' else 'DEU ÍMPAR')

        if escolha == tipo:
            print('VOCÊ VENCEU!')
            vitorias += 1
        else:
            print('VOCÊ PERDEU!')
            break
        print('Vamos jogar novamente...')

    print(f'GAME OVER! Você venceu {vitorias} vezes.\033[m')
    
    repetir = str(input('Deseja repetir o programa? [S/N] ')).strip().upper()[0]
    if repetir == 'N':
        break