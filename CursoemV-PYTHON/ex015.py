print('====== 15 ======')

km = float(input('Quantos quilometros você rodou? '))
dias = int(input('Quantos dias vc ficou com o carro? '))
dias = dias * 60
km = km * 0.15
print(f'O valor a pagar é {dias:.2f} dias e {km:.2f} por Km rodade {dias + km:.2f}')
