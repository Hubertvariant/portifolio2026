from time import sleep

c = {0: '\033[m', 1: '\033[36m', 2: '\033[33m', 4: '\033[32m', 5:'\033[31m'}

print(f'{c[1]}=' * 20)
print(f'{c[2]}ex034')
print(f'{c[1]}={c[0]}' * 20)

sal = int(input('Digite o seu salario: '))
if sal > 1250:
    sal = sal + (sal * 10/100)
    aumen = 10
else:
    sal = sal + (sal * 15/100)
    aumen = 15

sleep(2)
print(f'O seu salario recebeu um {c[4]}aumento{c[0]} de {c[4]}{aumen}%{c[0]} e agora é {c[4]}{sal:.2f}{c[0]}')