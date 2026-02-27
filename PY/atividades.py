print('Menu de atividades')
print('1) Dobro, Triplo e Raiz quadrada')
print('2) Média aritmética')
print('3) Conversão de reais para dolar')
print('4) conversor de medidas')
opcao = int(input('Digite uma opção: '))

if opcao == 1:
    print('1) Dobro, Triplo e Raiz quadrada')
    n = int(input('Digite um numero: '))
    print(f'Dobro {n * 2}')
    print(f'Triplo {n * 3}')
    print(f'Raiz quadrada {n ** (1/2)}')

elif opcao == 2:
    print('2) Média aritmética')
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

elif opcao == 3:
    print('3) Conversão de reais para dolar')
    n = int(input('Digite o valor para converter para dolar: '))
    print(f'US${n / 5.14:2f}')

elif opcao == 4:
    print('4) conversor de medidas')
    k = int(input('Digite uma medida em kilometros: '))
    print(f'{k} metros = {k / 100} m')
    print(f'{k} metros = {k / 1000} cm')
