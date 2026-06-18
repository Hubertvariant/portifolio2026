c = {0: '\033[m', 1: '\033[36m', 2: '\033[33m', 4: '\033[32m', 5:'\033[31m'}

print(f'{c[1]}=' * 20)
print(f'{c[2]}ex029')
print(f'{c[1]}={c[0]}' * 20)

vel = int(input(f'{c[5]}Senhor individo{c[0]}, vc tá correndo? Qual é a tua velocidade EX[99]? '))
if vel > 80:
    print(f'{c[5]}Você está sendo multado!!{c[0]}')
    print(f'O valor da sua multa é de {c[5]}R${(vel - 80) * 7:.2f}{c[0]}')
print(f'{c[2]}Parabens! Continue com cuidado.{c[0]}')