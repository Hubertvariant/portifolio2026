cores = {0: '\033[m', 1: '\033[31;1m'}

print(f'{cores[1]}=' * 10)
print(f'{"ex044":^10}')
print('=' * 10)

print('\033[1;33mPagando\033[m \033[1;36mProdutos\033[m')

preco = float(input('\033[1mDigite o preço do produto: R$'))
print('\033[1;36mDinheiro\033[m \033[1mou \033[1;33mCartão\033[m')
formaP = str(input('\033[1mDigite a forma de pagamento: ')).strip().lower()

if formaP == 'dinheiro':
    print(f'Pagamento a vista: R${preco - (preco * 10 / 100):.2f}')
else:
    formaX = int(input('\033[1mQuantas vezes no cartão? '))
    if formaX == 1:
        print(f'Á vista no cartão: R${preco - (preco * 5 / 100):.2f}')
    elif formaX == 2:
        print(f'Em 2x: R${preco:.2f}')
    else:
        if formaX != 3:
            print('O maximo é 3x (aplicando juros de 3x)')
        print(f'Em 3x: R${preco + (preco * 20 / 100):.2f}')