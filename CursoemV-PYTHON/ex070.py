from time import sleep

while True:
    print(f'\033[1;36m{"=" * 10}\n{"ex070":^10}\n{"=" * 10}\033[m\033[1m')
    sleep(1)

    soma = prod1000 = baratoPreco = cont = 0
    baratoNome = ''

    print(f'{"_" * 20}\n{"LOJA SUPER BARATÃO":^20}\n{"_" * 20}')

    while True:
        prodNome = str(input('Nome do Produto: ')).strip().capitalize()
        prodPreco = float(input('Preço: R$'))
        cont += 1
        soma += prodPreco

        if prodPreco > 1000:
            prod1000 += 1

        if cont == 1 or prodPreco < baratoPreco:
            baratoPreco = prodPreco
            baratoNome = prodNome

        continuar = ' '
        while continuar not in 'SN':
            continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if continuar == 'N':
            break

    print(f'{" FIM DO PROGRAMA ":-^40}')
    print(f'O total da compra foi R${soma:.2f}')
    print(f'Temos {prod1000} produtos custando mais de R$1000.00')
    print(f'O produto mais barato foi {baratoNome} que custa R${baratoPreco:.2f}')

    repetir = str(input('Deseja repetir o programa? [S/N] ')).upper().strip()[0]
    if repetir == 'N':
        break