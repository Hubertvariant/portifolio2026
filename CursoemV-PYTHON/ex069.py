from time import sleep

while True:
    print(f'\033[1;36m{"=" * 10}\n{"ex069":^10}\n{"=" * 10}\033[m\033[1m')
    sleep(1)

    maiores = homens = mulheresMenores = 0

    while True:
        print(f'{"_" * 20}\n{"CADASTRE UMA PESSOA":^20}\n{"_" * 20}')
        idade = int(input('Idade: '))
        sexo = ' '
        while sexo not in 'MF':
            sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
        
        if idade >= 18:
            maiores += 1
        if sexo == 'M':
            homens += 1
        if sexo == 'F' and idade < 20:
            mulheresMenores += 1

        continuar = ' '
        while continuar not in 'SN':
            continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if continuar == 'N':
            break

    print(f'Total de pessoas com mais de 18 anos: {maiores}')
    print(f'Ao todo temos {homens} homens cadastrados.')
    print(f'E temos {mulheresMenores} mulheres com menos de 20 anos.')

    repetir = str(input('Deseja repetir o programa? [S/N] ')).upper().strip()[0]
    if repetir == 'N':
        break