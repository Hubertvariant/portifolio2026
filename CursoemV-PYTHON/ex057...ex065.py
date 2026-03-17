from time import sleep
from random import randint
from math import factorial
import pygame
pygame.init()
pygame.mixer.init()
res = 'S'

while res == 'S':
    ex = str(input('Exercicio: '))
    if ex.isnumeric():
        ex = int(ex)
    if ex == 57:
        print(f'''\033[1;33m{'=' * 10}
{'ex057':^10}
{'=' * 10}\033[m''')
        sleep(1)

        print('\033[1;34mVerificador\033[m \033[1mde \033[1;33mDados\033[m')
        sexo = str(input('\033[1mDigite seu sexo: \033[m')).strip()
        while sexo not in 'MmFf':
            print('\033[1;31m[ERRO!]\033[m')
            sexo = str(input('\033[1mDigite seu sexo novamente: \033[m')).upper().strip()

    elif ex == 58:
        print(f'\033[1;33m{'=' * 10}\n{'ex058':^10}\n{'=' * 10}\033[m')
        sleep(1)

        print('\033[1;33mJogo\033[m \033[1mde \033[1;34madivinhação\033[m \033[1mV2.0 \nIrei pensar em um número entre 0 e 10 \nTente adivinhar')
        sleep(1)
        print('\033[37mpensando...\033[m\033[1m')
        sleep(3)
        compNum = randint(0, 10)

        palpite = int(input('Qual é o seu palpite? '))
        numPalpites = 1

        while palpite != compNum:

            if compNum > palpite:
                print('Mais...')
            else:
                print('Menor...')

            palpite = int(input('\033[31;1mVocê errou!!\033[m\n\033[1mTente novamente: '))

            numPalpites += 1

        print(f'\033[32;1mParabens!!\033[m \033[1mvocê \033[32;1macertou!!\033[m\n\033[1mPrecisou de {numPalpites} palpites para acertar')

    elif ex == 59:

        print(f'\033[1;33m{'=' * 10}\n{'ex059':^10}\n{'=' * 10}\033[m')
        sleep(1)

        print('\033[1mCalculadora!')
        sleep(1)

        opcao = 0
        testeNum = False

        while not testeNum:
            n1 = str(input('Digite um número: '))
            n2 = str(input('Digite outro número: '))

            if n1.isnumeric() and n2.isnumeric():
                n1 = int(n1)
                n2 = int(n2)
                testeNum = True
            else:
                print('\033[1;31m[ERRO!]\033[m')
                sleep(1)
                print('TENTE NOVAMENTE!')

        while opcao != 5:

            sleep(1)
            print('''[1]SOMA
[2]MULTIPLICAR
[3]MAIOR
[4]NOVOS NÚMEROS
[5]SAIR DO PROGRAMA''')
            sleep(1)

            opcao = int(input('Qual será a sua escolha? '))
            sleep(1)
            if opcao != 5:
                if opcao == 1:

                    print(f'{n1} + {n2} = {n1 + n2}')

                elif opcao == 2:

                    print(f'{n1} x {n2} = {n1 * n2}')

                elif opcao == 3:

                    maior = 0

                    if n1 > n2:
                        maior = n1
                    else:
                        maior = n2

                    print(f'O maior número digitado foi {maior}')

                elif opcao == 4:

                    n1 = int(input('Digite um número: '))
                    n2 = int(input('Digite outro número: '))

                else:

                    print('\033[1;31m[ERRO!]\033[m Tente novamente')

            else:
                print('Volte sempre!\033[m')
                sleep(1)

    elif ex == 59001:

        print(f'\033[1;33m{'=' * 10}\n{'ex059':^10}\n{'=' * 10}\033[m')
        sleep(1)

        print('\033[1;34mCalculadora\033[m')

        opcao = ''

        while opcao != 'sair':
            num1 = int(input('Digite um número para a operação: '))
            num2 = int(input('Digite outro número para a operação: '))
            opcao = str(input('''Escolha uma das operações
[1]SOMA
[2]SUBTRAÇÃO
[3]MULTIPLICAÇÃO
[4]DIVISÃO
[60]FATORIAL
DIGITE "sair" PARA SAIR
''')).lower().strip()
            if  not opcao.isnumeric():
                opcao = 'sair'
            else:
                opcao = int(opcao)
                if opcao == 60:
                    print(f'Considerando o primeiro digito: {num1}')
                    fat = 1
                    c = 1
                    while c <= num1:
                        fat *= c
                        c += 1
                    print(f'{num1}! = {fat}')
                else:
                    if opcao == 1:
                        resultado0 = num1 + num2
                        resultado1 = '+'
                    elif opcao == 2:
                        resultado0 = num1 - num2
                        resultado1 = '-'
                    elif opcao == 3:
                        resultado0 = num1 * num2
                        resultado1 = 'x'
                    elif opcao == 4:
                        resultado0 = num1 / num2
                        resultado1 = '/'
                    print(f'{num1} {resultado1} {num2} = {resultado0}')

    elif ex == 60:

        print(f'\033[1;34m{'=' * 10}\n{'ex060':^10}\n{'=' * 10}\033[m')
        sleep(1)

        print('\033[1;33mFATORIAL!\033[m\033[1m')

        n = int(input('Digite um número para o calculo do fatorial: '))

        fat = factorial(n)
        c = n

        while c > 0:

            print(f'{c}', end='')
            print(' x ' if c > 1 else ' = ', end='')

            # fat *= c

            c -= 1

        print(fat)
        sleep(1)

    elif ex == 61:
        print(f'\033[1;34m{'=' * 10}\n{'ex061':^10}\n{'=' * 10}\033[m')
        sleep(1)

        print('termos com while')
        p1 = int(input('Digite o primeiro termo: '))
        raz = int(input('Digite a razão: '))
        razao = p1 + (10 - 1) * raz
        while p1 <= razao:
            print(p1, end=' -> ')
            p1 += raz
        print('FIM!')

    elif ex == 62:
        print(f'\033[1;34m{'=' * 10}\n{'ex062':^10}\n{'=' * 10}\033[m')
        sleep(1)

        print('termos com while 2.0')

        p1 = int(input('Digite o primeiro termo: '))
        raz = int(input('Digite a razão: '))

        if raz == 0:
            raz = 1

        res = 1
        i = 10

        while res != 0:

            razao = p1 + (i - 1) * raz

            while p1 <= razao:

                print(p1, end=' -> ')

                p1 += raz

            res = str(input('\nDeseja adicionar mais quantos termos? '))
            while not res.isnumeric():
                print(f'\033[1;31m[ERRO!] [{res}]\033[m\033[1m É invalido, tente novamente.')
                res = str(input('\n\033[1mDeseja adicionar mais quantos termos?\033[m '))
            res = int(res)

            if res != 0:

                i = res

        print('FIM!')

    elif ex == 63:
        print(f'\033[1;34m{'=' * 10}\n{'ex063':^10}\n{'=' * 10}\033[m')
        sleep(1)

        print('Fibonacci series')

        n = int(input('Digite o n-ésimo número: '))

        i = 1
        f1 = 0
        f3 = 1

        while i <= (n - 1):

            if i == 1:
                print('0', end=' -> ')

            print(f3, end=' -> ')

            if i == 1:
                f2 = 1

            f3 = f1 + f2
            f1 = f2
            f2 = f3

            i += 1

        print('FIM!')

    elif ex == 64:

        print(f'\033[1;33m{'=' * 10}\n{'ex064':^10}\n{'=' * 10}\033[m')
        sleep(1)

        print('Números')

        num = 1
        soma = 0
        tentativas = 0
        stringstext = ['Digite números', 'tentativa']

        while num != 999:

            num = float(input(f'{stringstext[0]} EX[999]: '))

            if num != 999:

                tentativas += 1
                stringstext[0] = 'Você errou tente novamente'
                stringstext[1] = 'tentativas'

                soma += num

        print(f'FIM!\nVocê precisou de {tentativas} {stringstext[1]} até digitar o número 999\nO resulta da soma de todos os digitos exeto o flag é {int(soma)}')

    elif ex == 65:

        print(f'\033[1;33m{'=' * 10}\n{'ex065':^10}\n{'=' * 10}\033[m\033[1m')

        condicao = ''
        soma = 0
        tentativas = 0

        while condicao != 'N':

            if tentativas == 0:
                numero = int(input('Digite um número: '))
                menor = maior = numero

            else:
                numero = int(input('Digite outro número: '))

            if numero > maior:
                maior = numero

            if numero < menor:
                menor = numero

            tentativas += 1
            soma += numero
            condicao = ''

            while 'S' != condicao != 'N':
                condicao = str(input(f'\033[1;36mDeseja continuar?[S/N]\033[m ')).strip().upper()

        print(f'A média de todos os {tentativas} números digitados é: {soma/tentativas}\nO maior número foi {maior}\nO menor número foi {menor}', end='')
        print('\033[m')

    else:
        pygame.mixer.music.load('lestGo.mp3')
        pygame.mixer.music.play()
        pygame.event.wait()
        while pygame.mixer.music.get_busy():
            sleep(1)