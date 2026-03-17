while True:
    print(f'\033[1;36m{"=" * 10}\n{"ex066":^10}\n{"=" * 10}\033[m')
    print('\033[1mPrograma dos Números 2.0')
    soma = cont = 0
    
    while True:
        numero = int(input('Digite um número [999 para parar]: '))
        if numero == 999:
            break
        soma += numero
        cont += 1
    
    print(f'Foram digitados \033[1;36m{cont}\033[m números e a soma entre eles foi \033[1;36m{soma}\033[m')

    repetir = str(input('Deseja repetir o programa? [S/N] ')).strip().upper()
    if repetir == 'N':
        break