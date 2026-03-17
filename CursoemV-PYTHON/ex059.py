from time import sleep

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
    
    if opcao == 1:
        print(f'{n1} + {n2} = {n1 + n2}')
    elif opcao == 2:
        print(f'{n1} x {n2} = {n1 * n2}')
    elif opcao == 3:
        maior = n1 if n1 > n2 else n2
        print(f'O maior número digitado foi {maior}')
    elif opcao == 4:
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
    elif opcao == 5:
        print('Volte sempre!\033[m')
    else:
        print('\033[1;31m[ERRO!]\033[m Tente novamente')