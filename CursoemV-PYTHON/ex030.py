c = {0: '\033[m', 1: '\033[36m', 2: '\033[33m', 4: '\033[32m', 5:'\033[31m'}

print(f'{c[1]}=' * 20)
print(f'{c[2]}ex030')
print(f'{c[1]}={c[0]}' * 20)

print(f'{c[1]}Você sabe se o número é par ou impar?')
print(f'teste para saber{c[0]}')
n = int(input('Digite um número: '))
if n % 2 == 0:
    print(f'{n} é {c[4]}PAR{c[0]}')
else:
    print(f'{n} é {c[5]}IMPAR{c[0]}')