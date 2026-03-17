while True:
    print(f'\033[1;36m{"=" * 10}\n{"ex067":^10}\n{"=" * 10}\033[m')
    
    while True:
        number = int(input('\033[1mDigite o Número para a Tabuada (negativo para parar): '))
        if number < 0:
            break
        
        print(f'{"-" * 15}')
        for cont in range(1, 11):
            print(f'{number} X {cont} = {number * cont}')
        print(f'{"-" * 15}')
    
    repetir = str(input('Deseja repetir o programa? [S/N] ')).strip().upper()
    if repetir == 'N':
        break