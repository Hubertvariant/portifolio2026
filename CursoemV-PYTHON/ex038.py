from time import sleep

cores = {0: '\033[m', 1: '\033[31;1m'}

print(f'{cores[1]}=' * 10)
print(f'{"ex038":^10}')
print(f'=' * 10, f'{cores[0]}')
sleep(1)

print('Vamos comparar dois números!')
numero0 = int(input('Digite o primeiro número: '))
numero1 = int(input('Digite o segundo número: '))
sleep(1)

if numero0 == numero1:
    print(f'\033[1;33mNão existe{cores[0]}\033[1m um valor maior, os dois são \033[36;1miguais\033[m')
elif numero0 > numero1:
    print('O\033[1;33m primeiro valor\033[m\033[1m é \033[36;1mmaior\033[m')
else:
    print('O\033[1;33m segundo valor\033[m\033[1m é \033[36;1mmaoir\033[m')
sleep(1)