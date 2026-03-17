from time import sleep

print('\033[33;1m=' * 10)
print(f'{"ex049":^10}')
print('=' * 10, '\033[m')
sleep(1)

print('\033[1mTABUADA! DE NOVO MAS TÁ MELHOR!\033[m')

tabuada = int(input('Digite o numero da tabuada: '))
limitedaTabuada = int(input('Digite o limite da tabuada: [min:10/max:100] '))

if limitedaTabuada < 10:
    limitedaTabuada = 10
elif limitedaTabuada > 100:
    limitedaTabuada = 100

for c in range(0, limitedaTabuada + 1):
    print(f'\033[1m{tabuada} x {c} = {tabuada * c}\033[m')