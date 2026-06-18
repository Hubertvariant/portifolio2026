from time import sleep

cores = {0: '\033[m', 1: '\033[31;1m'}

print(f'{cores[1]}=' * 10)
print(f'{"ex037":^10}')
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
        numcon = bin(numero)
        con = 'binário'
    elif opcao == 2:
        numcon = oct(numero)
        con = 'octal'
    elif opcao == 3:
        numcon = hex(numero)
        con = 'hexadecimal'
    else:
        print('\033[7[ERRO!]\033[m')
        numcon = ""
        con = ""
    
    if con != "":
        print(f'A conversão do {numero} para {con}: {numcon[2:]}')
else:
    print('Ok, Obrigado por participar!')
sleep(1)