print(f'\033[1;33m{'=' * 10}\n{'ex065':^10}\n{'=' * 10}\033[m\033[1m')

res = 'S'
soma = quant = média = maior = menor = 0

while res in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    res = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]

média = soma / quant
print(f'Você digitou {quant} números e a média foi {média}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
print('\033[m')