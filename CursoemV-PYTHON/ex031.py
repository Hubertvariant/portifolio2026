c = {0: '\033[m', 1: '\033[36m', 2: '\033[33m', 4: '\033[32m', 5:'\033[31m'}

print(f'{c[1]}=' * 20)
print(f'{c[2]}ex031')
print(f'{c[1]}={c[0]}' * 20)

viag = int(input('Qual a distancia da sua viagem em KM: '))
if viag <= 200:
    print(f'O preço da passagem será de {c[5]}R${viag * 0.5:.2f}{c[0]}')
else:
    print(f"O preço da passagem será de {c[5]}R${viag * 0.45:.2f}{c[0]}")