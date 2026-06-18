import pygame
from time import sleep
from random import randint
from datetime import date
pygame.init()
cores = {0: '\033[m', 1: '\033[31;1m'}
ex = int(input('Qual ex? '))
if ex == 36:

    print(f'{cores[1]}=' * 10)
    print(f'{'ex036':^10}')
    print('=' * 10, f'{cores[0]}')

    sleep(1)

    print(f'Vamos calcular o valor do impréstimo da casa.')
    sleep(1)
    casa = float(input('Qual o valor da casa? '))
    salario = float(input('Qual o seu salario? '))
    anos = int(input('Em quantos anos você deseja parcelar? '))
    sleep(1)
    valor = casa / (anos * 12)
    if valor > salario * 30 / 100:
        print(f'O valor mensal do emprestimo é de \033[1m{valor:.2f}\033[m')
        print('O emprestimo \033[1;31mNÃO\033[m foi aprovado!')
    else:
        print(f'O valor mensal do emprestimo é de \033[1m{valor:.2f}\033[m')
        print('O emprestimo \033[1;32mFOI\033[m aprovado!')

    sleep(1)
elif ex == 37:
    print(f'{cores[1]}=' * 10)
    print(f'{'ex037':^10}')
    print('=' * 10, f'{cores[0]}')

    sleep(1)

    print('Conversão de números.')
    sleep(1)
    numero = int(input('Qual número você deseja converter? '))
    print('Digite:')
    print('\033[1m1\033[m para binário.')
    print('\033[1m2\033[m para octal.')
    print('\033[1m3\033[m para hexadecimal.')
    print('\033[1m4\033[m para sair')
    sleep(1)
    opcao = int(input('Digite sua escolha: '))
    sleep(1)
    if opcao != 4:
        if opcao == 1:
            numcon: str = bin(numero)
            con: str = 'binário'
        elif opcao == 2:
            numcon: str = oct(numero)
            con: str = 'octal'
        elif opcao == 3:
            numcon: str = hex(numero)
            con: str = 'hexadecimal'

        else:
            print('\033[7[ERRO!]\033[m')
        print(f'A conversão do {numero} para {con}: {numcon[2:]}')
    else:
        print('Ok, Obrigado por participar!')
    sleep(1)
elif ex == 38:
    print(f'{cores[1]}=' * 10)
    print(f'{'ex038':^10}')
    print(f'=' * 10, f'{cores[0]}')
    sleep(1)

    print('Vamos comparar dois números!')
    numero0 = int(input('Digite o primeiro número: '))
    numero1 = int(input('Digite o segundo número: '))
    sleep(1)
    if numero0 == numero1:
        print(f'\033[1;33mNão existe{cores[0]}\033[1m um valor maior, os dois são \033[36;1miguais\033[m')
    elif numero0 > numero1:
        print('O\033[1;33m primeiro valor\033[m\033[1m é \033[36;1mmaior\033[m')
    else:
        print('O\033[1;33m segundo valor\033[m\033[1m é \033[36;1mmaoir\033[m')
    sleep(1)
elif ex == 39:
    print(f'{cores[1]}=' * 10)
    print(f'{'ex039':^10}')
    print(f'=' * 10, f'{cores[0]}')
    sleep(1)

    print('\033[1mSentido!\033[m Soldado!')
    atual = date.today().year
    nas = int(input('Quando você nasceu soldado? '))
    idade = atual - nas
    sleep(1)
    print(f'Soldado você tem {idade} anos.', end=' ')
    if idade < 17:
        print(f'Falta {17 - idade} anos. \033[1;33mAinda vai se alistar\033[m\033[1m ao serviço militar.')
    elif  idade < 19:
        print('\033[1;33mHora de se alistar.\033[m')
    else:
        print(f'{idade - 18} anos. \033[1;33mPassou do tempo\033[m \033[1mdo alistamento.\033[m')
    sleep(1)
elif ex == 40:
    print(f'{cores[1]}=' * 10)
    print(f'{'ex040':^10}')
    print('=' * 10, f'{cores[0]}')
    sleep(1)

    print('Leitor de média.')
    nome = str(input('Média do Aluno: ')).strip().capitalize()
    nota0 = float(input('Digite sua primeira nota: '))
    nota1 = float(input('Digite sua segunda nota: '))
    media = (nota0 + nota1) / 2
    print(f'\033[1mSUA MÉDIA É {media}')
    if media < 5:
        print('\033[1;31mREPROVADO!\033[m')
    elif 5 >= media < 7:
        print('\033[1;33mRECUPERAÇÃO!\033[m')
    else:
        print('\033[1;32mAPROVADO!\033[m')
elif ex == 41:
    print(f'{cores[1]}=' * 10)
    print(f'{'ex041':^10}')
    print('=' * 10, f'{cores[0]}')
    sleep(1)

    print('\033[1mConfederação Nacional de Natação!\033[m')
    sleep(1)

    ano = int(input('Digite seu ano de nascimento: '))
    atual = date.today().year
    idade = atual - ano
    sleep(1)
    print(f'\033[1m{idade} anos. \033[m', end='')
    print('\033[1;36m', end='')
    if idade <= 9:
        print('MIRIM')
    elif idade <= 14:
        print('INFANTIL')
    elif idade <= 19:
        print('JUNIOR')
    elif idade == 20:
        print('SENIOR')
    else:
        print('MASTER')
    print('\033[m')

elif ex == 42:

    print(f'{cores[1]}=' * 10)
    print(f'{'ex042':^10}')
    print('=' * 10, f'{cores[0]}')

    print('\033[1mTRIÂNGULOS\033[m')
    al = float(input('\033[33mQual o tamanho da reta a? '))
    bl = float(input('\033[32mQual o tamanho da reta b? '))
    cl = float(input('\033[36mQual o tamanho da reta c? \033[m'))
    sleep(1)

    if al < bl + cl and bl < cl + al and cl < al + bl:
        print('\033[33;1mÉ possivel montar um triangulo!\033[m\033[1;36m',end=' ')
        if al == bl == cl:
            print('Equilatero!', end='')
        elif al != bl != cl != al:
            print('Escaleno!', end='')
        else:
            print('Isosceles!', end='')
        print('\033[m')
    else:
        print('\033[31;1mNÃO\033[m \033[1mé possivel montar um triângulo!\033[m')

elif ex == 43:

    print(f'{cores[1]}=' * 10)
    print(f'{'ex043':^10}')
    print('=' * 10, f'{cores[0]}')

    print('\033[36;1mCalculadora\033[m \033[1mde\033[33m IMC\033[m')
    peso = float(input('\033[1mDigite o seu peso: '))
    altura = float(input('\033[1mDigite sua altura: '))
    imc = peso / altura ** 2
    sleep(1)
    if imc < 18.5:
        print(f'{imc:.1f}: Abaixo do peso.')
    elif imc < 25:
        print(f'{imc:.1f}: Peso ideal')
    elif imc < 30:
        print(f'{imc:.1f}: Sobrepeso')
    elif imc < 40:
        print(f'{imc:.1f}: Obesidade')
    else:
        print(f'{imc:.1f}: Obesidade mórbida')

elif ex == 44:

    print(f'{cores[1]}=' * 10)
    print(f'{'ex044':^10}')
    print('=' * 10)

    print('\033[1;33mPagando\033[m \033[1;36mProdutos\033[m')

    preco = float(input('\033[1mDigite o preço do produto: R$'))
    print('\033[1;36mDinheiro\033[m \033[1mou \033[1;33mCartão\033[m')
    formaP = str(input('\033[1mDigite a forma de pagamento: ')).strip().lower()
    if formaP == 'dinheiro':
        print(f'Pagamento a vista: R${preco * 10 / 100 - preco:.2f}')
    else:
        formaX = int(input('\033[1mQuantas vezes no cartão? '))
        if formaX == 1:
            print(f'Á vista no cartão: R${preco * 5 / 100 - preco:.2f}')
        elif formaX == 2:
            print(f'Em 2x: R${preco}')
        else:
            if formaX != 3:
                print('O maximo é 3x')
            print(f'Em 3x: R${preco * 20 / 100 + preco:.2f}')

elif ex == 45:

    print(f'{cores[1]}=' * 10)
    print(f'{'ex045':^10}')
    print('=' * 10, f'{cores[0]}')
    sleep(1)
    print('JOKENPÔ')
    sleep(1)
    print(f'''{'[PEDRA]':^9}
{'[PAPEL]':^9}
[TESOURA]''')
    sleep(1)

    player = str(input('Qual será a sua jogada? ')).strip().lower()
    sleep(1)
    print('\033[1;33mJO\033[m ')
    sleep(1)
    print('\033[1;33mKE\033[m ')
    sleep(1)
    print('\033[1;33mPÔ\033[m ')
    computador = randint(0, 2)
    item = ['Pedra', 'Papel', 'Tesoura']
    print(item[computador], end=' ')
    if computador == 0: #pedra
        if player == 'pedra':
            print('\033[33;1mEMPATE!\033[m')
        elif player == 'papel':
            print('\033[32;1mVITÓRIA!\033[m')
        elif player == 'tesoura':
            print('\033[31;1mDERROTA!\033[m')
        else:
            print('INVALIDO')
    elif computador == 1: #papel
        if player == 'papel':
            print('\033[33;1mEMPATE!\033[m')
        elif player == 'tesoura':
            print('\033[32;1mVITÓRIA!\033[m')
        elif player == 'pedra':
            print('\033[31;1mDERROTA!\033[m')
        else:
            print('INVALIDO')
    else: # tesoura
        if player == 'tesoura':
            print('\033[33;1mEMPATE!\033[m')
        elif player == 'pedra':
            print('\033[32;1mVITÓRIA!\033[m')
        elif player == 'papel':
            print('\033[31;1mDERROTA!\033[m')
        else:
            print('INVALIDO')
else:
    pygame.mixer.music.load('lestGo.mp3')
    pygame.mixer.music.play()
    pygame.event.wait()
    while pygame.mixer.music.get_busy():
        sleep(1)
