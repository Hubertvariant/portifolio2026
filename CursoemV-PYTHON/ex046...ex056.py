from time import sleep
import pygame
from datetime import date
pygame.init()
res = 'S'
while res == 'S':
    ex = str(input('Exercicio: '))
    if ex.isnumeric():
        ex = int(ex)
    if ex == 46:
        print('\033[33;1m=' * 10)
        print(f'{'ex046':^10}')
        print('=' * 10, '\033[m')
        sleep(1)

        print('\033[1mCONTAGEM REGRESSIVA!\033[m')
        sleep(1)
        for c in range(10, -1, -1):
            print(f'{c:^5}')
            sleep(1)
        print('\033[31;1mFIM!\033[m')

    elif ex == 47:
        print('\033[33;1m=' * 10)
        print(f'{'ex047':^10}')
        print('=' * 10, '\033[m')
        sleep(1)

        print('\033[1mNÚMEROS PARES!\033[m')
        sleep(1)
        for c in range(2, 51, 2):
            print(f'{c}...', end=' ')
        print('\033[1mFIM!\033[m')

    elif ex == 48:

        print('\033[33;1m=' * 10)
        print(f'{'ex048':^10}')
        print('=' * 10, '\033[m')
        sleep(1)

        print('\033[1mSOMA de números impares, divisiveis por 3, no intervalo de 1 áte 500\033[m'.upper())
        soma = 0
        cont = 0
        for c in range(1, 501, 2):
            if c % 3 == 0:
                cont += 1
                soma += c
        print(f'\033[33;1mA SOMA de todos os {cont} números impares, divisiveis por 3 e no intervalo de 1 áte 500: {soma}\033[m')

    elif ex == 49:

        print('\033[33;1m=' * 10)
        print(f'{'ex049':^10}')
        print('=' * 10, '\033[m')
        sleep(1)

        print('\033[1mTABUADA! DE NOVO MAS TÁ MELHOR!\033[m')

        tabuada = int(input('Digite o numero da tabuada: '))
        limitedaTabuada = int(input('Digite o limite da tabuada: [min:10/max:100] '))
        if limitedaTabuada < 10:
            limitedaTabuada = 10
        elif limitedaTabuada > 100:
            limitedaTabuada = 100

        for c in range(0, limitedaTabuada+1):
            print(f'\033[1m{tabuada} x {c} = {tabuada * c}\033[m')
    elif ex == 50:
        print('\033[33;1m=' * 10)
        print(f'{'ex050':^10}')
        print('=' * 10, '\033[m')
        sleep(1)

        soma = 0

        print('\033[1mDIGITE NÚMEROS!')
        for c in range(0, 6):
            num = int(input(f'Digite o {c + 1}°o número: '))
            if num % 2 == 0:
                soma += num
        print(f'A soma de todos os números pares digitados é igual a {soma}\033[m')
    elif ex == 51:

        print(f'''\033[33;1m{'=' * 10}
{'ex051':^10}
{'=' * 10}\033[m''')
        sleep(1)
        p1 = int(input('Digite o primeiro termo: '))
        razão = int(input('Digite a razão: '))
        for c in range(p1,(p1 + (10 - 1) * razão) + razão, razão ):
            print(c, end= ' -> ')
        print('Acabou!')

    elif ex == 52:

        print('\033[33;1m=' * 10)
        print(f'{'ex052':^10}')
        print('=' * 10, '\033[m')

        print('\033[1mIDENTIFICADOR DE NÚMEROS PRIMOS!')
        num = int(input('Digite um número: '))
        tot = 0
        for c in range(1, num + 1):
            if num % c == 0:
                print('\033[34;1m', end=' ')
                tot += 1
            else:
                print('\033[m', end=' ' )
            print(f'{c}',end='')
        print('\033[m')
        if tot > 2:
            print('\033[1mNão é primo!\033[m')
        else:
            print('\033[1mÉ primo!\033[m')
    elif ex == 53:

        print('\033[33;1m=' * 10)
        print(f'{'ex053':^10}')
        print('=' * 10, '\033[m')

        print('\033[1mReconhecedor de polindromo')
        frase = str(input('Digite uma frase: ')).replace(' ','').lower()
        print(f'\033[1mO inverso da palavra {frase} é {frase[::-1]}\033[m\033[1m')
        if frase[::-1] == frase:
            print('Essa frase é um \033[36;1mpolidromo\033[m!')
        else:
            print('Essa frase \033[31;1mnão\033[m \033[1mé um \033[36;1mpolidromo\033[m!')
    elif ex == 54:
        print('\033[33;1m=' * 10)
        print(f'{'ex054':^10}')
        print('=' * 10, '\033[m')
        sleep(1)

        print('\033[1mLeitor da maior idade.')
        ano = date.today().year
        maiorIdade = 0
        menorIdade = 0
        for c in range(0, 7):
            anoNas = int(input(f'Quando {c + 1}°o nasceu? '))
            if ano - anoNas >= 21:
                maiorIdade += 1
            else:
                menorIdade += 1
        print(f'''Maiores de idade: {maiorIdade}
Menor de Idade: {menorIdade}\033[m''')
    elif ex == 55:
        
        print('\033[33;1m=' * 10)
        print(f'{'ex055':^10}')
        print('=' * 10, '\033[m')
        sleep(1)
        
        pesoMaior = 0
        print('\033[1mPesometro')
        for c in range(0, 5):
            peso = float(input(f'Digite o peso do {c + 1}°o: '))
            if c == 0:
                pesoMaior = peso
                pesoMenor = peso
            else:
                if peso > pesoMaior:
                    pesoMaior = peso
                elif peso < pesoMenor:
                    pesoMenor = peso
        print(f'''Maior Peso foi: {pesoMaior}
Menor peso foi: {pesoMenor}\033[m''')
    elif ex == 56:
        print(f'''\033[33;1m{'=' * 10}
{'ex056':^10}
{'=' * 10}\033[m''')
        sleep(1)

        soma = 0
        homemVelho = 0
        mulheresNovas = 0
        print('\033[1mFORMULARIO!')
        for c in range(0, 4):
            print('-=' * 10)
            nome = str(input('Digite o seu nome: ')).capitalize().strip()
            idade = int(input('Digite sua idade: '))
            sexo = int(input('''Digite:
[1]Masculino
[2]Feminino
Digite o número do seu sexo: '''))
            soma += idade
            if sexo == 1:
                if idade > homemVelho:
                    homemVelho = idade
                    nomeVelho = nome
            else:
                if idade < 21:
                    mulheresNovas += 1
        print(f'''A média da idade do grupo: {soma / 4}
O homem mais velho é o {nomeVelho} com {homemVelho} anos
Número de mulheres abaixo de 21 anos: {mulheresNovas}''')
    else:
        pygame.mixer.init()
        pygame.mixer.music.load('lestGo.mp3')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            sleep(1)
    res = str(input('Deseja continuar? [S/N] ')).strip().upper()
