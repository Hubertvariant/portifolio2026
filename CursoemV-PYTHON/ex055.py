from time import sleep

print('\033[33;1m=' * 10)
print(f'{"ex055":^10}')
print('=' * 10, '\033[m')
sleep(1)

pesoMaior = 0
pesoMenor = 0
print('\033[1mPesometro')

for c in range(0, 5):
    peso = float(input(f'Digite o peso do {c + 1}°o: '))
    if c == 0:
        pesoMaior = peso
        pesoMenor = peso
    else:
        if peso > pesoMaior:
            pesoMaior = peso
        elif peso < pesoMenor:
            pesoMenor = peso

print(f'''Maior Peso foi: {pesoMaior}
Menor peso foi: {pesoMenor}\033[m''')