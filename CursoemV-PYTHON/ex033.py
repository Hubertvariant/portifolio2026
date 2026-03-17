from time import sleep

c = {0: '\033[m', 1: '\033[36m', 2: '\033[33m', 4: '\033[32m', 5:'\033[31m'}

print(f'{c[1]}=' * 20)
print(f'{c[2]}ex033')
print(f'{c[1]}={c[0]}' * 20)

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
n3 = int(input('Digite mais um valor: '))

sleep(2)
print(f'\033[1;41mOu você não tem medo de ficar digitando números sem saber o por que?\033[m')
sleep(1)

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