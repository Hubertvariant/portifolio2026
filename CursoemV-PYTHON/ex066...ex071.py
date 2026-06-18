from random import randint
from time import sleep

ex = str(input('QUAL EXERCICIO VOCÊ DESEJA ACESSAR?[66 ao 72] '))

if ex.isnumeric():
    ex = int(ex)

if ex == 66:
    while True:

        print(f'\033[1;36m{'=' * 10}\n{'ex066':^10}\n{'=' * 10}\033[m')
        print('\033[1mPrograma dos Números 2.0')
        soma = cont = 0
        while True:
            numero = int(input('Digite um número:[PARA SAIR 999] '))

            if numero == 999:
                break

            soma += numero
            cont += 1

        print(f'foram digitados \033[1;36m{cont}\033[m\033[1m e a soma entre eles foi \033[1;36m{soma}\033[m')

        #condição de parada
        repetir = str(input('Deseja repetir?[S/N] ')).strip().upper()

        if repetir == 'N':
            break

elif ex == 67:
    while True:

        print(f'\033[1;36m{'=' * 10}\n{'ex067':^10}\n{'=' * 10}\033[m')

        while True:

            number = int(input('\033[1mDigite o Número para a Tabuada: '))

            if number < 0:
                break

            print(f'{number:-^15}')

            for cont in range(1,11):
                print(f'{number} X {cont} = {number * cont}')

            print(f'-\033[m' * 15)

        #condição de parada
        repetir = str(input('Deseja repetir?[S/N] ')).strip().upper()

        if repetir == 'N':
            break

elif ex == 68:
    while True:

        print(f'\033[1;36m{'=' * 10}\n{'ex068':^10}\n{'=' * 10}\033[m')
        vitorias = 0
        while True:

            computer = randint(0, 10)

            number = int(input('\033[1mDiga um número: '))

            escolha = ' '

            while escolha not in 'IP':
                escolha = str(input('Par ou Impar?[P/I] ')).upper().strip()[0]

            print('PAR')
            sleep(1)
            print('OU')
            sleep(1)
            print('IMPAR')
            sleep(1)

            if (computer + number) % 2 == 0:
                if escolha == 'P':
                    resultado = 1
                    vitorias += 1
                else:
                    resultado = 0
            else:
                if escolha == 'I':
                    resultado = 1
                    vitorias += 1
                else:
                    resultado = 0

            if resultado == 0:
                print('derrota...', end=' ')
                print(f'DEU {computer + number}')
                break
            else:
                print('VITÓRIA!!!', end=' ')
                print(f'DEU {computer + number}')

        print(f'Total de vitórias {vitorias}\033[m')

        #condição de parada
        repetir = str(input('Deseja repetir?[S/N] ')).strip().upper()[0]

        if repetir in 'N':
            break

elif ex == 69:
    while True:
        print(f'\033[1;36m{'=' * 10}\n{'ex069':^10}\n{'=' * 10}\033[m\033[1m')
        sleep(1)

        maiores = homens = mulheresMenores = 0

        while True:
            print(f'{'_' * 20}\n{'CADASTRE UMA PESSOA':^20}\n{'_' * 20}')
            sleep(1)

            sexo = ' '
            while sexo not in 'MF':
                sexo = str(input('Digite o seu sexo:[M/F] ')).upper().strip()[0]
            idade = int(input('Digite sua idade: '))
            cadastraMais = ' '
            while cadastraMais not in 'SN':
                cadastraMais = str(input('Deseja cadastrar mais pessoas?[S/N] ')).upper().strip()[0]

            if idade >= 18:
                maiores += 1
            elif sexo in 'M':
                homens += 1
            elif sexo in 'F' and idade < 20:
                mulheresMenores += 1

            if cadastraMais in 'N':
                break

        print(f'{maiores} pessoas tem mais de 18 anos.\n'
              f'{homens} homens foram cadastrados.\n'
              f'{mulheresMenores} mulheres são menores de 20 anos.\033[m')

        #condição de parada
        repetir = str(input('Deseja repetir?[S/N]')).upper().strip()[0]

        if repetir in 'N':
            break
elif ex == 70:
    while True:
        print(f'\033[1;36m{'=' * 10}\n{'ex069':^10}\n{'=' * 10}\033[m\033[1m')
        sleep(1)

        soma = prod1000 = baratoPreco = cont = 0
        baratoNome = ' '

        print(f'{'_' * 20}\n{'Loja Americanas':^20}\n{'_' * 20}')
        sleep(1)

        while True:
            prodNome = str(input('Digite o nome do produto: ')).strip().capitalize()
            prodPreco = None
            while prodPreco is None:
                try:
                    precoInput = str(input('Digite o preço do produto: R$'))
                    prodPreco = float(precoInput)
                    if prodPreco <= 0:
                        print('O valor deve ser positivo')
                        prodPreco = None
                except ValueError:
                    print('Entrada invalida! Digite novamente.')
                    prodPreco = None

            soma += prodPreco

            if prodPreco >= 1000:
                prod1000 += 1

            if cont == 0 or prodPreco < baratoPreco:
                baratoPreco = prodPreco
                baratoNome = prodNome
                cont = 1


            continuar = ' '

            while continuar not in 'SN':
                continuar = str(input('Deseja continuar?[S/N] ')).upper().strip()[0]
            if continuar in 'N':
                break

        print(f'{'FIM DO PROGRAMA':-^20}')

        print(f'A soma de todos os produtos foi: {soma:.2f}\n'
              f'{prod1000} foi cadastrado acima de R$1000\n'
              f'O produto mais barato foi: {baratoNome} custando: R${baratoPreco:.2f}')

        #condição de parada
        repetir = str(input('Deseja repetir?[S/N] ')).upper().strip()[0]

        if repetir in 'N':
            break

if ex == 71:
    while True:
        print(f'\033[1;36m{'=' * 10}\n{'ex071':^10}\n{'=' * 10}\033[m\033[1m')
        sleep(1)

        print(f'{'CAIXA ELETRONICO':=^40}')
        sleep(1)

        sacar = ' '
        while not sacar.isnumeric():
            sacar = str(input('Digite o valor a ser sacado: R$'))
        sacar = int(sacar)

        montante = sacar
        nota = 50
        totNota = 0

        while True:
            if montante >= nota:
                montante -= nota
                totNota += 1
            else:
                if totNota != 0:
                    print(f'{totNota} nota(s) de {nota} reais.')

                if nota == 50:
                    nota = 20
                elif nota == 20:
                    nota = 10
                elif nota == 10:
                    nota = 1
                totNota = 0
                if montante == 0:
                    break

        print(f'{'VOLTE SEMPRE':=^40}')

        #condição de parada
        repetir = str(input('Deseja repetir?[S/N] ')).upper().strip()[0]

        if repetir == 'N':
            break
elif ex == 'seed':
    for c in range(1, 14):
        n = randint(0,9)
        print(n)
