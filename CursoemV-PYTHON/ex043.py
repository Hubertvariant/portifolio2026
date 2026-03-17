from time import sleep

cores = {0: '\033[m', 1: '\033[31;1m'}

print(f'{cores[1]}=' * 10)
print(f'{"ex043":^10}')
print('=' * 10, f'{cores[0]}')

print('\033[36;1mCalculadora\033[m \033[1mde\033[33m IMC\033[m')
peso = float(input('\033[1mDigite o seu peso: '))
altura = float(input('\033[1mDigite sua altura: '))
imc = peso / (altura ** 2)
sleep(1)

if imc < 18.5:
    print(f'{imc:.1f}: Abaixo do peso.')
elif imc < 25:
    print(f'{imc:.1f}: Peso ideal')
elif imc < 30:
    print(f'{imc:.1f}: Sobrepeso')
elif imc < 40:
    print(f'{imc:.1f}: Obesidade')
else:
    print(f'{imc:.1f}: Obesidade mórbida')