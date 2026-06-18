from time import sleep

while True:
    print(f'\033[1;36m{"=" * 10}\n{"ex071":^10}\n{"=" * 10}\033[m\033[1m')
    sleep(1)

    print(f'{"=" * 40}\n{"BANCO CEV":^40}\n{"=" * 40}')
    valor = int(input('Que valor você quer sacar? R$'))
    montante = valor
    ced = 50
    totced = 0
    
    while True:
        if montante >= ced:
            montante -= ced
            totced += 1
        else:
            if totced > 0:
                print(f'Total de {totced} cédulas de R${ced}')
            if ced == 50:
                ced = 20
            elif ced == 20:
                ced = 10
            elif ced == 10:
                ced = 1
            totced = 0
            if montante == 0:
                break
                
    print(f'{"=" * 40}\nVolte sempre ao BANCO CEV! Tenha um bom dia!')

    repetir = str(input('Deseja repetir o programa? [S/N] ')).upper().strip()[0]
    if repetir == 'N':
        break