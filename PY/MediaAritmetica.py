print('Média aritmética')
cont = 0
soma = 0
while True:
    n = int(input('Digite um numero: '))
    soma = soma + n
    cont = cont + 1
    opcao = str(input('Deseja adicionar mais um numero?[S/N] ')).strip().upper()
    if opcao == 'N':
        break

print(f'A média aritimética é: {soma /cont}')
