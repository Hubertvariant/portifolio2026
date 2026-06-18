from random import randint
from datetime import date
from time import sleep

c = {0: '\033[m', 1: '\033[36m', 2: '\033[33m', 4: '\033[32m', 5:'\033[31m'}
print(f'{c[1]}=' * 20)
print(f'{c[2]}ex028')
print(f'{c[1]}={c[0]}' * 20)

print(f'Vou pensar em um numero entre 0 e 5,{c[1]} tente adivinhar{c[0]}!!!')
print('pensando...')
sleep(2)
nC = int(randint(0, 5))
nU = int(input('Ok. que número eu pensei? '))
sleep(2)
print(f'Você {c[4]}acertou{c[0]}!!! meu número era {nC}' if nC == nU else f'Você {c[5]}errou{c[0]}! meu número era {nC}')

print(f'{c[1]}=' * 20)
print(f'{c[2]}ex029')
print(f'{c[1]}={c[0]}' * 20)

vel = int(input(f'{c[5]}Senhor individo{c[0]}, vc tá correndo? Qual é a tua velocidade EX[99]? '))
if vel > 80:
    print(f'{c[5]}Você está sendo multado!!{c[0]}')
    print(f'O valor da sua multa é de {c[5]}R${(vel - 80) * 7:.2f}{c[0]}')
print(f'{c[2]}Parabens! Continue com cuidado.{c[0]}')

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

print(f'{c[1]}=' * 20)
print(f'{c[2]}ex031')
print(f'{c[1]}={c[0]}' * 20)

viag = int(input('Qual a distancia da sua viagem em KM: '))
if viag <= 200:
    print(f'O preço da passagem será de {c[5]}R${viag * 0.5:.2f}{c[0]}')
else:
    print(f"O preço da passagem será de {c[5]}R${viag * 0.45:.2f}{c[0]}")

print(f'{c[1]}=' * 20)
print(f'{c[2]}ex032')
print(f'{c[1]}={c[0]}' * 20)

ano = str(input('Em que ano você está EX[9999]? '))
if ano == 0 or ano == '':
    ano = date.today().year
else:
    ano = int(ano)
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'{ano} {c[4]}é bissexto!')
else:
    print(f'{ano} {c[5]}não é bissexto!')

print(f'{c[1]}=' * 20)
print(f'{c[2]}ex033')
print(f'{c[1]}={c[0]}' * 20)

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
n3 = int(input('Digite mais um valor: '))
sleep(2)
print(f'\033[1;41mOu você não tem medo de ficar digitando números sem saber o por que?\033[m')
sleep(10)
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
elif n3 > n1 and n3 > n2:
    maior = n3

if n1 < n2 and n1 < n3:
    menor = n1
elif n2 < n1 and n2 < n3:
    menor = n2
else:
    menor = n3
print(f'{c[5]}O menor número é {menor}')
print(f'{c[4]}O maior número é {maior}')

print(f'{c[1]}=' * 20)
print(f'{c[2]}ex034')
print(f'{c[1]}={c[0]}' * 20)

sal = int(input('Digite o seu salario: '))
if sal > 1250:
    sal = sal + sal * 10/100
    aumen = 10
else:
    sal = sal + sal * 15/100
    aumen = 15
sleep(2)
print(f'O seu salario recebeu um {c[4]}aumento{c[0]} de {c[4]}{aumen}%{c[0]} e agora é {c[4]}{sal:.2f}{c[0]}')

print('=' * 20)
print('ex035')
print('=' * 20)

aL = float(input(f'{c[2]}Digite o primeiro lado do triângulo: '))
bL = float(input(f'{c[1]}Digite o segundo lado do triângulo: '))
cL = float(input(f'{c[4]}Digite o terceiro lado do triângulo: '))
if aL < bL + cL and bL < aL + cL and cL < aL + bL:
    print(f'{c[0]}As retas {c[2]}a:{aL}{c[0]}, {c[1]}b:{bL}{c[0]} e {c[4]}c:{cL}{c[0]} podem{c[0]} forma um triângulo!')
else:
    print(f'{c[0]}As retas {c[2]}a:{aL}{c[0]}, {c[1]}b:{bL}{c[0]} e {c[4]}c:{cL}{c[0]} {c[5]}não podem{c[0]} forma um triângulo!')

