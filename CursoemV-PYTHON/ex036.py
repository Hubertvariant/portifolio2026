from time import sleep

cores = {0: '\033[m', 1: '\033[31;1m'}

print(f'{cores[1]}=' * 10)
print(f'{"ex036":^10}')
print('=' * 10, f'{cores[0]}')

sleep(1)

print(f'Vamos calcular o valor do impréstimo da casa.')
sleep(1)
casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o seu salario? '))
anos = int(input('Em quantos anos você deseja parcelar? '))
sleep(1)
valor = casa / (anos * 12)

if valor > salario * 30 / 100:
    print(f'O valor mensal do emprestimo é de \033[1m{valor:.2f}\033[m')
    print('O emprestimo \033[1;31mNÃO\033[m foi aprovado!')
else:
    print(f'O valor mensal do emprestimo é de \033[1m{valor:.2f}\033[m')
    print('O emprestimo \033[1;32mFOI\033[m aprovado!')

sleep(1)