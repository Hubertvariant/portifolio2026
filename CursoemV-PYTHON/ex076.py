from random import randint

contCor = randint(0, 1)
cor = ('\033[1;36m', '\033[1;33m')

print(f'{cor[contCor]}{"076":=^40}\033[m')
lista_de_materiais = ('Lápis', 1.00, 'Cola', 3.00, 'Tesoura', 3.00, 'Bolsa', 65.00, 'Caderno', 24.00, 'Caneta', 1.50)

print('-=-' * 13)
print(f'{"LISTA DE MATERIAIS":^39}')
print('-=-' * 13)

for pos in range(0, len(lista_de_materiais)):
    if pos % 2 == 0:
        print(f'{lista_de_materiais[pos]:.<30}', end='')
    else:
        print(f'R${lista_de_materiais[pos]:>7.2f}')

print('-=-' * 13)