from random import randint

contCor = randint(0, 1)
cor = ('\033[1;36m', '\033[1;33m')

print(f'{cor[contCor]}{"80":=^40}\033[m')
listaDeValores = []

for c in range(0, 5):
    add = int(input('Digite o valor: '))
    if c == 0 or add > listaDeValores[-1]:
        listaDeValores.append(add)
        print('Adicionado no final da lista.')
    else:
        for pos, v in enumerate(listaDeValores):
            if add <= v:
                listaDeValores.insert(pos, add)
                print(f'Adicionado na posição {pos} da lista')
                break

print(f'Os valores digitados em ordem foram: {listaDeValores}')